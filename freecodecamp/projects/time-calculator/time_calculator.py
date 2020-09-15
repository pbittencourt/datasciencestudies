#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def numbertoampm(hour, minute):
    if hour < 12 or hour == 24:
        period = 'AM'
    else:
        period = 'PM'
    hour = hour % 12
    if hour == 0:
        hour = 12
    return (hour, minute, period)


def ampmtonumber(time):
    hour, minute, period = time.split(':')
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
    minute = int(minute)
    return (hour, minute, period)


def add_time(start, duration, weekday=''):
    """
    Add the duration time to the start time and return the result.

    :start: time in the 12-hour clock format (ending in AM or PM) -> str
    :duration: time that indicates the number of hours and minutes -> str
    :day_week: (optional) starting day of the week, case insensitive -> str
    :returns: TODO
    """

    # days of the week
    days = (
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    )

    # splitting data
    start = start.strip().replace(' ', ':')
    hour, minute, period = ampmtonumber(start)
    hour_delta, minute_delta = duration.strip().split(':')
    hour_delta = int(hour_delta)
    minute_delta = int(minute_delta)

    # sum of minutes
    minute_sum = minute + minute_delta
    hours_ahead = 0
    if minute_sum >= 60:
        hours_ahead = minute_sum // 60
    hour_delta += hours_ahead
    new_minute = minute_sum - 60 * hours_ahead

    # sum of hours
    hour_sum = hour + hour_delta
    days_ahead = 0
    if hour_sum > 24:
        days_ahead = hour_sum // 24
    new_hour = hour_sum - 24 * days_ahead

    # number to AM/PM
    new_hour, new_minute, period = numbertoampm(new_hour, new_minute)
    new_time = f'{new_hour}:{str(new_minute).zfill(2)} {period}'

    # day of the week
    if weekday.strip() != '':
        weekday = weekday.strip().title()
        weekindex = days.index(weekday)
        new_weekindex = (weekindex + days_ahead) % 7
        new_weekday = days[new_weekindex]
        new_time += ', ' + new_weekday

    # time shift: how many days ahead?
    if days_ahead == 0:
        pass
    elif days_ahead == 1:
        new_time += ' (next day)'
    else:
        new_time += f' ({days_ahead} days later)'

    return new_time


if __name__ == "__main__":
    print(add_time("10:45 PM", "3:30", "Monday"))
    print(add_time("11:30 AM", "2:32"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30", "TueSday"))
    print(add_time("11:43 PM", "24:20", 'wednesday'))
    print(add_time("6:30 PM", "205:12", 'SAtURdaY'))
