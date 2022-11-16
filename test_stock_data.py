import unittest
import stock_data
import numpy as np


class TestHistoricData(unittest.TestCase):
    def test_create(self):
        hd1 = stock_data.HistoricData(['2002', '2003', '2022'], np.array([10, 20, 30]), np.array([11, 21, 31]),
                                      np.array([12, 22, 32]), np.array([13, 23, 33]))
        hd2 = stock_data.HistoricData(['2012', '2013', '2022'], np.array([20, 30, 40]), np.array([21, 31, 41]),
                                      np.array([22, 32, 42]), np.array([23, 33, 43]))

        self.assertEqual(hd1.dates, ['2002', '2003', '2022'])
        self.assertTrue((hd1.closes == np.array([10, 20, 30])).all())
        self.assertTrue((hd1.opens == np.array([11, 21, 31])).all())
        self.assertTrue((hd1.highs == np.array([12, 22, 32])).all())
        self.assertTrue((hd1.lows == np.array([13, 23, 33])).all())

        self.assertEqual(hd2.dates, ['2012', '2013', '2022'])
        self.assertTrue((hd2.closes == np.array([20, 30, 40])).all())
        self.assertTrue((hd2.opens == np.array([21, 31, 41])).all())
        self.assertTrue((hd2.highs == np.array([22, 32, 42])).all())
        self.assertTrue((hd2.lows == np.array([23, 33, 43])).all())


if __name__ == '__main__':
    unittest.main()
