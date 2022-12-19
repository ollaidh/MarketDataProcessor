import unittest
from marketdata import config


class TestConfig(unittest.TestCase):
    def test_config_with_period(self):
        # GIVEN
        #   json with period for stock data presented as period
        # WHEN
        #   parsing config from json
        # THEN
        #   parameters after calling function should be equal to input, except "start_date" and "end_date" which should be None
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
        self.assertIsNone(conf.start_date)
        self.assertIsNone(conf.end_date)
        self.assertEqual(conf.price, inp1["price"])
        self.assertEqual(conf.processor, inp1["processor"])

    def test_config_with_period_format(self):
        # GIVEN
        #   json with period for stock data passed incorretly: period, start date and end date at the same time
        # WHEN
        #   parsing config from json
        # THEN
        #   parameters after calling function should be equal to input, except "period" which should be None
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

    def test_config_with_startend(self):
        # GIVEN
        #   json with period for stock data presented as start date and end date
        # WHEN
        #   parsing config from json
        # THEN
        #   parameters after calling function should be equal to input, except "period" which should be None
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
        self.assertIsNone(conf.period)
        self.assertEqual(conf.interval, inp3["interval"])
        self.assertEqual(conf.start_date, inp3["start_date"])
        self.assertEqual(conf.end_date, inp3["end_date"])
        self.assertEqual(conf.price, inp3["price"])
        self.assertEqual(conf.processor, inp3["processor"])


if __name__ == '__main__':
    unittest.main()
