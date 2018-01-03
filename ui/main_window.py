# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from constant.param import SENDING_TIME_HOURS, SENDING_TIME_MIN
from lib.timestamp import timestamp_now, timestamp_to_date, timestamp_to_hour, timestamp_at_time


class MainWindow(QMainWindow):
    """
    Fenêtre Qt.
    """

    def __init__(self):
        """
        Crée une nouvelle instance de `QMainWindow`
        """
        super(MainWindow, self).__init__()
        self.time_label = QLabel("Initialisation en cour")
        self.status_label = QLabel("En attente demande d'envoie")
        self.last_send = QLabel("Dernier mail: Aucun mail envoyé")
        self.next_send = QLabel()
        self.update_next_send()
        self.init_widget()

    def init_widget(self):
        central_widget = QWidget(parent=self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.status_label)
        vbox.addWidget(self.last_send)
        vbox.addWidget(self.next_send)
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

    def update_next_send(self, ts=None):
        ts = ts if ts else timestamp_at_time(timestamp_now(), hours=SENDING_TIME_HOURS, min=SENDING_TIME_MIN)
        send_date = timestamp_to_date(ts)
        send_time = timestamp_to_hour(ts)
        self.next_send.setText("Prochain mail: Le {date} à {time}".format(date=send_date, time=send_time))

    def watch_signals(self, new_second, send_in_progress, send_completed):
        new_second.connect(self.handle_new_second)
        send_in_progress.connect(self.handle_send_in_progress)
        send_completed.connect(self.handle_send_completed)

    def handle_new_second(self):
        ts = timestamp_now()
        time = timestamp_to_hour(ts)
        self.time_label.setText(time)

    def handle_send_in_progress(self):
        self.status_label.setText("Envoie en cour")

    def handle_send_completed(self, new_end):
        self.status_label.setText("En attente demande d'envoie")
        ts = timestamp_now()
        last_send_date = timestamp_to_date(ts)
        last_send_time = timestamp_to_hour(ts)
        self.last_send.setText("Dernière mail: Le {date} à {time}".format(date=last_send_date, time=last_send_time))
        self.update_next_send(new_end)
