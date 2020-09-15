#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ampm2number(hour, period):
    if period == 'AM':
        if hour == '12':
            hour = 0
        else:
            hour = int(hour)
    else:
        if hour == '12':
            hour = 12
        else:
            hour = int(hour) + 12
    return hour


def numbertoampm(time):
    hour = int(time)
    if hour < 12 or hour == 24:
        period = 'AM'
    else:
        period = 'PM'
    hour = hour % 12
    if hour == 0:
        hour = 12
    print(f'Was {time}:00 and now is {hour} {period}.')


def add_time(start, duration, day_week=None):
    """
    Add the duration time to the start time and return the result.

    :start: time in the 12-hour clock format (ending in AM or PM) -> str
    :duration: time that indicates the number of hours and minutes -> str
    :day_week: (optional) starting day of the week, case insensitive -> str
    :returns: TODO
    """

    # splitting data
    start = start.strip().replace(' ', ':')
    hour, minute, period = start.split(':')
    hour = ampm2number(hour, period)
    print(hour)
    minute = int(minute)

    hour_delta, minute_delta = duration.strip().split(':')
    hour_delta = int(hour_delta)
    minute_delta = int(minute_delta)

    # sum of hours
    hour_sum = hour + hour_delta
    print(hour_sum)
    print(hour_sum // 24)
    print(hour_sum % 24)

numbertoampm('1')
numbertoampm('2')
numbertoampm('3')
numbertoampm('4')
numbertoampm('5')
numbertoampm('6')
numbertoampm('7')
numbertoampm('8')
numbertoampm('9')
numbertoampm('10')
numbertoampm('11')
numbertoampm('12')
numbertoampm('13')
numbertoampm('14')
numbertoampm('15')
numbertoampm('16')
numbertoampm('17')
numbertoampm('18')
numbertoampm('19')
numbertoampm('20')
numbertoampm('21')
numbertoampm('22')
numbertoampm('23')
numbertoampm('24')
