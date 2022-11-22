import unittest
from marketdata import config


class TestConfig(unittest.TestCase):
    def test_config(self):
        inp1 = {"company": ["IBM", "TSLA"], "period": "1m", "interval": "1d"}
        conf = config.parse_config(inp1)
        self.assertEqual(conf.company, inp1["company"])
        self.assertEqual(conf.period, inp1["period"])
        self.assertEqual(conf.interval, inp1["interval"])


if __name__ == '__main__':
    unittest.main()
