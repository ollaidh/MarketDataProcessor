import unittest

from marketdata import historicdata
from marketdata.utils import date_from_year
import numpy as np


class TestHistoricData(unittest.TestCase):
    def test_create(self):
        hd1 = [
            historicdata.HistoricData(
                "IBM", [date_from_year(2002), date_from_year(2003), date_from_year(2004)], np.array([10, 20, 30])),
            historicdata.HistoricData(
                "TSLA", [date_from_year(2002), date_from_year(2003), date_from_year(2004)], np.array([11, 21, 31])),
            historicdata.HistoricData(
                "APPL", [date_from_year(2002), date_from_year(2003), date_from_year(2004)], np.array([10, 20, 30]))
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


if __name__ == '__main__':
    unittest.main()
