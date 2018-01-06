# !/usr/bin/env python
# -*- coding: utf-8 -*-

import locale
from datetime import datetime, timedelta


def timestamp_to_date(timestamp):
    """
    Calcul une date à partir d'un time
    :param timestamp: Le timestamp étudié
    :return: Un string du type "mercredi 03 janvier 2018"
    """
    locale.setlocale(locale.LC_TIME, '')
    return datetime.fromtimestamp(timestamp).strftime('%A %d %B %Y')


def timestamp_to_hour(timestamp):
    locale.setlocale(locale.LC_TIME, '')
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')


def timestamp_to_day(timestamp):
    locale.setlocale(locale.LC_TIME, '')
    return datetime.fromtimestamp(timestamp).strftime('%A')


def timestamp_now():
    """
    Calcul le timestamp actuel
    :return: Le timestamp actuel
    """
    now = datetime.now()
    return datetime(year=now.year,
                    month=now.month,
                    day=now.day,
                    hour=now.hour,
                    minute=now.minute,
                    second=now.second,
                    microsecond=now.microsecond).timestamp()


def timestamp_at_time(ts, hours=0, min=0, sec=0, microsecond=0):
    d = datetime.fromtimestamp(ts)
    return datetime(year=d.year,
                    month=d.month,
                    day=d.day,
                    hour=hours,
                    minute=min,
                    second=sec,
                    microsecond=microsecond).timestamp()


def timestamp_after_day_ago(start, day_ago=0, hour=0, min=0):
    now = datetime.fromtimestamp(start) + timedelta(days=day_ago)
    return datetime(year=now.year,
                    month=now.month,
                    day=now.day,
                    hour=hour,
                    minute=min,
                    second=0,
                    microsecond=0).timestamp()


def timestamp_to_inverse_date(timestamp):
    locale.setlocale(locale.LC_TIME, '')
    return datetime.fromtimestamp(timestamp).strftime('%Y_%m_%d')
