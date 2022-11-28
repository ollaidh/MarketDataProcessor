import unittest
from marketdata import config


class TestConfig(unittest.TestCase):
    def test_config(self):
        inp1 = {"tickers": ["IBM", "TSLA"], "period": "1m", "interval": "1d", "price": ["open", "close"]}
        conf = config.parse_config(inp1)
        self.assertEqual(conf.tickers, inp1["tickers"])
        self.assertEqual(conf.period, inp1["period"])
        self.assertEqual(conf.interval, inp1["interval"])
        self.assertEqual(conf.price, inp1["price"])


if __name__ == '__main__':
    unittest.main()
