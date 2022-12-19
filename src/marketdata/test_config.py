import unittest
from marketdata import config


class TestConfig(unittest.TestCase):
    def test_config(self):
        inp1 = {
            "tickers": ["IBM", "TSLA"],
            "period": "1m",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": "minmax"}
        }
        conf = config.parse_config(inp1)
        self.assertEqual(conf.tickers, inp1["tickers"])
        self.assertEqual(conf.period, inp1["period"])
        self.assertEqual(conf.interval, inp1["interval"])
        self.assertEqual(conf.start_date, None)
        self.assertEqual(conf.end_date, None)
        self.assertEqual(conf.price, inp1["price"])
        self.assertEqual(conf.processor, inp1["processor"])

        inp2 = {
            "tickers": ["IBM", "TSLA"],
            "period": "1m",
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": "minmax"}
        }
        self.assertRaises(config.InvalidPeriodParameters, config.parse_config, inp2)

        inp3 = {
            "tickers": ["IBM", "TSLA"],
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": "minmax"}
        }
        conf = config.parse_config(inp3)
        self.assertEqual(conf.tickers, inp3["tickers"])
        self.assertEqual(conf.period, None)
        self.assertEqual(conf.interval, inp3["interval"])
        self.assertEqual(conf.start_date, inp3["start_date"])
        self.assertEqual(conf.end_date, inp3["end_date"])
        self.assertEqual(conf.price, inp3["price"])
        self.assertEqual(conf.processor, inp3["processor"])


if __name__ == '__main__':
    unittest.main()
