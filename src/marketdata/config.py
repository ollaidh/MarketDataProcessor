import json
from dataclasses import dataclass
from typing import Optional


class InvalidPeriodParameters(Exception):
    def __str__(self):
        return 'Invalid period parameters! Expected: period OR start and end dates!'


@dataclass(frozen=True)
class Config:
    tickers: list[str]
    interval: str
    price: list[str]
    processor: {}
    period: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


def parse_config(parameters: dict):
    if 'period' in parameters and 'start_date' not in parameters and 'end_date' not in parameters:
        return Config(tickers=parameters['tickers'], interval=parameters['interval'], price=parameters['price'],
                      processor=parameters['processor'], period=parameters['period'])
    if 'start_date' in parameters and 'end_date' in parameters and 'period' not in parameters:
        return Config(tickers=parameters['tickers'],  interval=parameters['interval'], price=parameters['price'], processor=parameters['processor'],
                  start_date=parameters['start_date'], end_date=parameters['end_date'])
    raise InvalidPeriodParameters


def load_config_ffile(json_path):
    with open(json_path, 'r') as json_file:
        stock_parameters = json.load(json_file)
    # print(parse_config(stock_parameters))
    return parse_config(stock_parameters)


def load_config_fstring(line):
    stock_parameters = json.loads(line)
    return parse_config(stock_parameters)
