import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    tickers: list[str]
    period: str
    interval: str
    price: list[str]
    processor: str


def parse_config(parameters):
    return Config(parameters['tickers'], parameters['period'], parameters['interval'], parameters['price'],
                  parameters['processor'])


def load_config_ffile(json_path):
    with open(json_path, 'r') as json_file:
        stock_parameters = json.load(json_file)
    return parse_config(stock_parameters)


def load_config_fstring(line):
    stock_parameters = json.loads(line)
    return parse_config(stock_parameters)
