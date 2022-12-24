import json
from dataclasses import dataclass
from typing import Optional


class NoTicker(Exception):
    def __str__(self):
        return 'No tickers were found!'

class NoPeriod(Exception):
    def __str__(self):
        return 'No period was found!'

class InvalidPeriodParameters(Exception):
    def __str__(self):
        return 'Invalid period parameters! Expected: period OR start and end dates!'

class NoInterval(Exception):
    def __str__(self):
        return 'No interval was found!'

class NoPrice(Exception):
    def __str__(self):
        return 'No price was found!'

class NoProcessor(Exception):
    def __str__(self):
        return 'No processor was found!'


@dataclass(frozen=True)
class Config:
    tickers: list[str]
    interval: str
    price: list[str]
    processor: {}
    period: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


def validate_config(parameters: dict):
    def validate_tickers():
        if 'tickers' not in parameters or parameters['tickers'] == []:
            raise NoTicker

    def validate_period():
        if 'start_date' not in parameters and 'end_date' not in parameters and 'period' not in parameters:
            raise NoPeriod
        if 'start_date' in parameters and 'end_date' in parameters and 'period' in parameters:
            raise InvalidPeriodParameters
        if ('start_date' in parameters or 'end_date' in parameters) and 'period' in parameters:
            raise InvalidPeriodParameters

    def validate_interval():
        if 'interval' not in parameters or parameters['interval'] == []:
            raise NoInterval

    def validate_price():
        if 'price' not in parameters or parameters['price'] == []:
            raise NoPrice

    def validate_processor():
        if 'processor' not in parameters or parameters['processor'] == {}:
            raise NoProcessor
        if 'type' not in parameters['processor'] or parameters['processor']['type'] == []:
            raise NoProcessor

    validate_tickers()
    validate_period()
    validate_interval()
    validate_price()
    validate_processor()


def parse_config(parameters: dict):
    validate_config(parameters)
    if 'period' in parameters:
        return Config(tickers=parameters['tickers'], interval=parameters['interval'], price=parameters['price'],
                      processor=parameters['processor'], period=parameters['period'])
    if 'start_date' in parameters and 'end_date' in parameters:
        return Config(tickers=parameters['tickers'],  interval=parameters['interval'], price=parameters['price'], processor=parameters['processor'],
                  start_date=parameters['start_date'], end_date=parameters['end_date'])


def load_config_ffile(json_path):
    with open(json_path, 'r') as json_file:
        stock_parameters = json.load(json_file)
    return parse_config(stock_parameters)


def load_config_fstring(line):
    stock_parameters = json.loads(line)
    return parse_config(stock_parameters)
