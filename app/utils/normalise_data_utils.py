from datetime import datetime

from app.custom_exceptions import IncorrectDatetimeFormatException


def to_upper(s):
    return s.upper()


def to_2_decimal_places(fl):
    return round(fl, 2)


def normalise_name(s):
    return s.replace(' ', '-').replace('_', '-')


def to_datetime(s):
    try:
        res = str(datetime.strptime(s, '%Y-%m-%d %H:%M:%S').utcnow())
    except ValueError as e:
        raise IncorrectDatetimeFormatException(e)
    else:
        return res
