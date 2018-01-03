# !/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import locale
import os
import time

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def timestamp_to_date(timestamp):
    locale.setlocale(locale.LC_TIME, '')
    return datetime.fromtimestamp(timestamp).strftime('%A %d %B %Y')


def timestamp_now():
    now = datetime.now()
    return datetime(year=now.year,
                    month=now.month,
                    day=now.day,
                    hour=now.hour,
                    minute=now.minute,
                    second=now.second,
                    microsecond=now.microsecond).timestamp()


def send_mail():
    msg = MIMEMultipart()
    msg['From'] = 'audric.perrin@dune-sa.fr'
    msg['To'] = 'audric.perrin@dune-sa.fr'
    msg['Subject'] = "Rapport production bobine du {}".format(timestamp_to_date(timestamp_now()))
    message =\
"""Bonjour,

Ci-joint le rapport de production du jour.

Cordialement,


Audric Perrin
DUNE SA
24 Avenue Urbain Le Verrier
69800 ST PRIEST - France
Tél.04.72.37.39.67
www.dune-sa.fr
"""
    msg.attach(MIMEText(message))
    f_path = "I:\Programme mondon/rp_prod/2018_01_03 Rapport production bobines.pdf"
    f_name = "2018_01_03 Rapport production bobines.pdf"
    cover_letter = MIMEApplication(open(f_path, "rb").read())
    cover_letter.add_header('Content-Disposition', 'attachment', filename=f_name)
    msg.attach(cover_letter)

    mailserver = smtplib.SMTP('smtp.outlook.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('audric.perrin@dune-sa.fr', 'Loda6027')
    mailserver.sendmail('audric.perrin@dune-sa.fr', 'audric.perrin@dune-sa.fr', msg.as_string())
    mailserver.quit()

os.chdir("I:\Programme mondon\mondon-client_2")
os.system("start /B DUNE_production_bobines.exe")
time.sleep(10)
print("end_sleep")
os.system("taskkill /im DUNE_production_bobines.exe")
send_mail()
