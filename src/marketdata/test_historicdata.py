import unittest

from marketdata import historicdata
from marketdata.utils import date_from_years
import numpy as np
import pandas as pd


class TestHistoricData(unittest.TestCase):
    def test_create(self):
        hd1 = [
            historicdata.HistoricData(
                "IBM", date_from_years([2002, 2003, 2004]), np.array([10, 20, 30])),
            historicdata.HistoricData(
                "TSLA", date_from_years([2002, 2003, 2004]), np.array([11, 21, 31])),
            historicdata.HistoricData(
                "APPL", date_from_years([2002, 2003, 2004]), np.array([10, 20, 30]))
        ]
        hd2 = [
            historicdata.HistoricData(
                "NTFLX", date_from_years([2012, 2013, 2014, 2015]),
                np.array([110, 120, 130, 140])),
            historicdata.HistoricData(
                "FB", date_from_years([2012, 2013, 2014, 2015]),
                np.array([111, 121, 131, 141])),
            historicdata.HistoricData(
                "INST", date_from_years([2012, 2013, 2014, 2015]),
                np.array([112, 122, 132, 142]))
        ]

        # test hd1 case:
        self.assertEqual(len(hd1), 3)
        self.assertEqual(hd1[0].company, "IBM")
        self.assertEqual(hd1[1].company, "TSLA")
        self.assertEqual(hd1[2].company, "APPL")
        self.assertEqual(len(hd1[0].dates), 3)
        self.assertEqual(len(hd1[1].dates), 3)
        self.assertEqual(len(hd1[2].dates), 3)
        self.assertTrue((hd1[0].price == np.array([10, 20, 30])).all())
        self.assertTrue((hd1[1].price == np.array([11, 21, 31])).all())

        # test hd2 case:
        self.assertEqual(len(hd2), 3)
        self.assertEqual(hd2[0].company, "NTFLX")
        self.assertEqual(hd2[1].company, "FB")
        self.assertEqual(hd2[2].company, "INST")
        self.assertEqual(len(hd2[0].dates), 4)
        self.assertEqual(len(hd2[1].dates), 4)
        self.assertEqual(len(hd2[2].dates), 4)
        self.assertTrue((hd2[0].price == np.array([110, 120, 130, 140])).all())
        self.assertTrue((hd2[1].price == np.array([111, 121, 131, 141])).all())

        pddf = pd.DataFrame({'Close': [10, 20, 30], 'Open': [20, 40, 60]}, index=date_from_years([2012, 2013, 2014]))

        # test calc_average_price function:
        self.assertTrue((historicdata.calc_average_price(pddf, ['close', 'open']) == np.array([15, 30, 45])).all())
        self.assertTrue((historicdata.calc_average_price(pddf, ['close']) == np.array([10, 20, 30])).all())


if __name__ == '__main__':
    unittest.main()
