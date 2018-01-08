# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from lib.timestamp import timestamp_now, timestamp_to_date, timestamp_to_inverse_date


def go_send_mail():
    """
    Génère un rapport et envoie un mail avec le rapport
    """
    def generate_rapport():
        """
        S'occupe d'ouvrir le programme mondon-client et de le refermer
        A l'ouverture mondon-client génère le rapport du jour
        """
        # Ajout le chemin du .exe du programme mondon-client
        os.chdir("I:\Programme mondon\mondon-client_2")
        # Exécute en tâche de fond le programme
        os.system("start DUNE_production_bobines.exe --rapport")
    generate_rapport()
    time.sleep(30)
    send_mail()


def send_mail():
    msg = MIMEMultipart()
    msg['Subject'] = "Rapport production de bobines du {}".format(timestamp_to_date(timestamp_now()))
    msg['From'] = 'audric.perrin@dune-sa.fr'
    msg['To'] = 'audric.perrin@dune-sa.fr,nicolas.cormier@dune-sa.fr'
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
    f_path = "I:\Programme mondon/rp_prod/{} Rapport production bobines.pdf".format(timestamp_to_inverse_date(timestamp_now()))
    f_name = "{} Rapport production bobines.pdf".format(timestamp_to_inverse_date(timestamp_now()))
    cover_letter = MIMEApplication(open(f_path, "rb").read())
    cover_letter.add_header('Content-Disposition', 'attachment', filename=f_name)
    msg.attach(cover_letter)

    mailserver = smtplib.SMTP('smtp.outlook.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('audric.perrin@dune-sa.fr', 'Loda6027')
    mailserver.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
    mailserver.quit()
