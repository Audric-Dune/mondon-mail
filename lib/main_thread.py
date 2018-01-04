# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from PyQt5.QtCore import pyqtSignal, QThread

from constant.param import SENDING_TIME_HOURS, SENDING_TIME_MIN
from lib.timestamp import timestamp_now, timestamp_at_time, timestamp_after_day_ago, timestamp_to_day
from lib.mail import go_send_mail


class MainThread(QThread):
    ON_TIME_CHANGED = pyqtSignal()
    ON_SEND_IN_PROGRESS = pyqtSignal()
    ON_SEND_COMPLETED = pyqtSignal(int)

    SLEEP_TIME_MS = 1000
    SLEEP_ON_ERROR_MS = 1000

    def __init__(self):
        """
        Crée une nouvelle instance de MainThread
        """
        QThread.__init__(self)
        self.end = timestamp_at_time(timestamp_now(), hours=SENDING_TIME_HOURS, min=SENDING_TIME_MIN)

    @staticmethod
    def is_weekend(ts_day):
        """
        Test si un ts correspond à un jour du weekend (samedi ou dimanche)
        :return: True si le ts correspond a un samedi ou dimanche sinon False
        """
        day = timestamp_to_day(ts_day)
        return day == "samedi" or day == "dimanche"

    def run(self):
        try:
            while True:
                self.ON_TIME_CHANGED.emit()
                now = timestamp_now()
                if now > self.end:
                    self.ON_SEND_IN_PROGRESS.emit()
                    go_send_mail()
                    we = True
                    while we:
                        self.end = timestamp_after_day_ago(self.end,
                                                           day_ago=1,
                                                           hour=SENDING_TIME_HOURS,
                                                           min=SENDING_TIME_MIN)
                        we = self.is_weekend(self.end)

                    self.ON_SEND_COMPLETED.emit(self.end)
                self.msleep(self.SLEEP_TIME_MS)
        except:
            self.msleep(MainThread.SLEEP_ON_ERROR_MS)
            self.run()
