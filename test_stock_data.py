import unittest

import pandas as pd

import stock_data
import numpy as np


class TestHistoricData(unittest.TestCase):
    def test_create(self):
        def dtyr(year: int) -> pd.Timestamp: # create timestamp date from year only
            return pd.Timestamp(year=year, month=1, day=1, hour=1, minute=1, second=1)

        hd1 = stock_data.HistoricData([dtyr(2002), dtyr(2003), dtyr(2004)],
                                      np.array([10, 20, 30]),
                                      np.array([11, 21, 31]),
                                      np.array([12, 22, 32]),
                                      np.array([13, 23, 33]))
        hd2 = stock_data.HistoricData([dtyr(2012), dtyr(2013), dtyr(2014)],
                                      np.array([20, 30, 40]),
                                      np.array([21, 31, 41]),
                                      np.array([22, 32, 42]),
                                      np.array([23, 33, 43]))

        self.assertEqual(len(hd1.dates), 3)
        self.assertEqual(hd1.dates[0].year, 2002)
        self.assertEqual(hd1.dates[1].year, 2003)
        self.assertEqual(hd1.dates[2].year, 2004)
        self.assertTrue((hd1.closes == np.array([10, 20, 30])).all())
        self.assertTrue((hd1.opens == np.array([11, 21, 31])).all())
        self.assertTrue((hd1.highs == np.array([12, 22, 32])).all())
        self.assertTrue((hd1.lows == np.array([13, 23, 33])).all())

        self.assertEqual(len(hd2.dates), 3)
        self.assertEqual(hd2.dates[0].year, 2012)
        self.assertEqual(hd2.dates[1].year, 2013)
        self.assertEqual(hd2.dates[2].year, 2014)
        self.assertTrue((hd2.closes == np.array([20, 30, 40])).all())
        self.assertTrue((hd2.opens == np.array([21, 31, 41])).all())
        self.assertTrue((hd2.highs == np.array([22, 32, 42])).all())
        self.assertTrue((hd2.lows == np.array([23, 33, 43])).all())


if __name__ == '__main__':
    unittest.main()
