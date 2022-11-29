import datetime


def date_from_years(years: list[int]) -> list[datetime.datetime]:  # create timestamp date from year only
    result = []
    for year in years:
        result.append(datetime.datetime(year=year, month=1, day=1, hour=1, minute=1, second=1))
    return result
