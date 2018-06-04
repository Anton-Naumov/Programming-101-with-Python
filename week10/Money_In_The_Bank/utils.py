import re
import time
import datetime
from exceptions import BruteForce


DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def validate_datetime_srting(datetime_string):
    datetime_re = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    datetime_string_re = f'{datetime_re}#\d+(#{datetime_re})?'
    if re.match(datetime_string_re, datetime_string) is None:
        raise Exception('Invalid format of argument!')


def add_one_entry_to_datetime_string(datetime_string, currdt):
    validate_datetime_srting(datetime_string)
    dt_of_last, entries, penalty_start = get_datetime_componets(datetime_string)
    penalty_duration = (entries / 5) * 5 if (entries / 5) * 5 != 0 else 5
    updated_message = ''

    if dt_of_last + datetime.timedelta(minutes=penalty_duration) < currdt and penalty_start is None:
        updated_message = f'{currdt.strftime(DATETIME_FORMAT)}#1'
    elif entries % 5 == 0 and penalty_start + \
            datetime.timedelta(minutes=penalty_duration) > currdt:
        penalty_left = get_difference_between_datetimes_in_minutes(currdt, penalty_start +
                                                                   datetime.timedelta(minutes=penalty_duration))
        raise BruteForce('There are {} minutes penalty!'.format(int(penalty_left) + 1))
    elif (entries + 1) % 5 == 0:
        updated_message = f'{currdt.strftime(DATETIME_FORMAT)}#{entries + 1}#{currdt.strftime(DATETIME_FORMAT)}'
    else:
        updated_message = f'{currdt.strftime(DATETIME_FORMAT)}#{entries + 1}'

    return updated_message


def get_datetime_componets(datetime_string):
    """
    1 = date and time of last successfull entry
    2 = number of failed entries since the last successfull entrys
    3 = time of last penalty start or None if there is no penalty started

    format = 1#2#3
    """
    validate_datetime_srting(datetime_string)

    parts = datetime_string.split('#')

    dt = datetime.datetime.strptime(parts[0], DATETIME_FORMAT)
    number_of_entries = int(parts[1])
    penalty_start = None

    if len(parts) == 3:
        penalty_start = datetime.datetime.strptime(parts[2], DATETIME_FORMAT)

    return dt, number_of_entries, penalty_start


def get_difference_between_datetimes_in_minutes(dt1, dt2):
    d1_ts = time.mktime(dt1.timetuple())
    d2_ts = time.mktime(dt2.timetuple())

    return int(d2_ts-d1_ts) / 60
