import datetime


def date_from_year(year: int) -> datetime.datetime:  # create timestamp date from year only
    return datetime.datetime(year=year, month=1, day=1, hour=1, minute=1, second=1)