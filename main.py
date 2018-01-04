# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from lib.main_thread import MainThread
from ui.main_window import MainWindow

app = QApplication(sys.argv)
app.setWindowIcon(QIcon('assets/mail.ico'))

thread = MainThread()
thread.start()

window = MainWindow()
window.watch_signals(thread.ON_TIME_CHANGED, thread.ON_SEND_IN_PROGRESS, thread.ON_SEND_COMPLETED)
window.setWindowTitle("Send mail")
window.show()

sys.exit(app.exec_())
