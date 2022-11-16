import json
from dataclasses import dataclass
import unittest


@dataclass(frozen=True)
class Config:
    company: str
    period: str
    interval: str


def parse_config(parameters):
    return Config(parameters['company'], parameters['period'], parameters['interval'])


def load_config_ffile(json_name):
    with open(json_name, 'r') as json_file:
        stock_parameters = json.load(json_file)
    return parse_config(stock_parameters)


def load_config_fstring(line):
    stock_parameters = json.loads(line)
    return parse_config(stock_parameters)


if __name__ == '__main__':
    pass

