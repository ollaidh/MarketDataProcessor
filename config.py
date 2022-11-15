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


def test():
    inp = {"company": "IBM", "period": "1m", "interval": "1d"}
    config = parse_config(inp)
    assert config.company == inp["company"]
    assert config.period == inp["period"]
    assert config.interval == inp["interval"]


class TestConfig(unittest.TestCase):
    def test_config(self):
        inp1 = {"company": "IBM", "period": "1m", "interval": "1d"}
        config = parse_config(inp1)
        self.assertEqual(config.company, inp1["company"])
        self.assertEqual(config.period, inp1["period"])
        self.assertEqual(config.interval, inp1["interval"])


if __name__ == '__main__':
    unittest.main()

