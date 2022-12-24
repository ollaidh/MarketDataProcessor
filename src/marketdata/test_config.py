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
            "processor": {"type": ["minmax"]}
        }
        conf = config.parse_config(inp1)
        self.assertEqual(conf.tickers, inp1["tickers"])
        self.assertEqual(conf.period, inp1["period"])
        self.assertEqual(conf.interval, inp1["interval"])
        self.assertIsNone(conf.start_date)
        self.assertIsNone(conf.end_date)
        self.assertEqual(conf.price, inp1["price"])
        self.assertEqual(conf.processor, inp1["processor"])

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
            "processor": {"type": ["minmax"]}
        }
        conf = config.parse_config(inp3)
        self.assertEqual(conf.tickers, inp3["tickers"])
        self.assertIsNone(conf.period)
        self.assertEqual(conf.interval, inp3["interval"])
        self.assertEqual(conf.start_date, inp3["start_date"])
        self.assertEqual(conf.end_date, inp3["end_date"])
        self.assertEqual(conf.price, inp3["price"])
        self.assertEqual(conf.processor, inp3["processor"])


    def test_config_with_no_tickers(self):
        # GIVEN
        #   json with no "tickers" field or "tickers" list is empty
        # WHEN
        #   validating config
        # THEN
        #   raises NoTicker exception
        inp4 = {
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": ["minmax"]}
        }
        inp5 = {
            "tickers": [],
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": ["minmax"]}
        }
        self.assertRaises(config.NoTicker, config.validate_config, inp4)
        self.assertRaises(config.NoTicker, config.validate_config, inp5)


    def test_config_with_no_period(self):
        # GIVEN
        #   json with no "period" or "start_date" and "end_date" fields
        # WHEN
        #   validating config
        # THEN
        #   raising NoPeriod exception
        inp6 = {
            "tickers": ["IBM", "TSLA"],
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": ["minmax"]}
        }
        self.assertRaises(config.NoPeriod, config.validate_config, inp6)

    def test_config_with_period_format(self):
        # GIVEN
        #   json with period for stock data passed incorretly: period, start date and end date at the same time
        # WHEN
        #   validating config
        # THEN
        #   raises InvalidPeriodParameters exception
        inp7 = {
            "tickers": ["IBM", "TSLA"],
            "period": "1m",
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": ["minmax"]}
        }
        self.assertRaises(config.InvalidPeriodParameters, config.validate_config, inp7)

    def test_config_with_no_interval(self):
        # GIVEN
        #   json with no "interval" field
        # WHEN
        #   validating config
        # THEN
        #   raises NoInterval exception
        inp8 = {
            "tickers": ["IBM", "TSLA"],
            "period": "1m",
            "price": ["open", "close"],
            "processor": {"type": ["minmax"]}
        }
        self.assertRaises(config.NoInterval, config.validate_config, inp8)

    def test_config_with_no_price(self):
        # GIVEN
        #   json with no "price" field or "price" list is empty
        # WHEN
        #   validating config
        # THEN
        #   raises NoPrice exception
        inp9 = {
            "tickers": ["IBM", "TSLA"],
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "processor": {"type": ["minmax"]}
        }
        inp10 = {
            "tickers": ["IBM", "TSLA"],
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": [],
            "processor": {"type": ["minmax"]}
        }
        self.assertRaises(config.NoPrice, config.validate_config, inp9)
        self.assertRaises(config.NoPrice, config.validate_config, inp10)

    def test_config_with_no_processors(self):
        # GIVEN
        #   json with no "processor" field or "processor" dict is empty or processor['type'] list is empty
        # WHEN
        #   validating config
        # THEN
        #   raises NoProcessor exception
        inp11 = {
            "tickers": ["IBM", "TSLA"],
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
        }
        inp12 = {
            "tickers": ["IBM", "TSLA"],
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {}
        }
        inp13 = {
            "tickers": ["IBM", "TSLA"],
            "start_date": "2021-12-12",
            "end_date": "2022-01-01",
            "interval": "1d",
            "price": ["open", "close"],
            "processor": {"type": []}
        }
        self.assertRaises(config.NoProcessor, config.validate_config, inp11)
        self.assertRaises(config.NoProcessor, config.validate_config, inp12)
        self.assertRaises(config.NoProcessor, config.validate_config, inp13)


if __name__ == '__main__':
    unittest.main()
