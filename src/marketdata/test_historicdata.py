import unittest

from marketdata import historicdata
from marketdata.utils import date_from_year
import numpy as np


class TestHistoricData(unittest.TestCase):
    def test_create(self):
        hd1 = [historicdata.HistoricData(
            "IBM", [date_from_year(2002), date_from_year(2003), date_from_year(2004)], np.array([10, 20, 30]), np.array([100, 200, 300]),
            np.array([1000, 2000, 3000]), np.array([1, 2, 3])),
            historicdata.HistoricData(
                "TSLA", [date_from_year(2002), date_from_year(2003), date_from_year(2004)], np.array([11, 21, 31]), np.array([110, 210, 310]),
                np.array([1100, 2100, 3100]), np.array([111, 211, 311])),
            historicdata.HistoricData(
                "APPL", [date_from_year(2002), date_from_year(2003), date_from_year(2004)], np.array([10, 20, 30]), np.array([100, 200, 300]),
                np.array([1000, 2000, 3000]), np.array([1, 2, 3]))]

        # test hd1 case:
        self.assertEqual(len(hd1), 3)
        self.assertEqual(hd1[0].company, "IBM")
        self.assertEqual(hd1[1].company, "TSLA")
        self.assertEqual(hd1[2].company, "APPL")
        self.assertEqual(len(hd1[0].dates), 3)
        self.assertEqual(len(hd1[1].dates), 3)
        self.assertEqual(len(hd1[2].dates), 3)
        self.assertTrue(
            (hd1[0].closes == np.array([10, 20, 30])).all())
        self.assertTrue(
            (hd1[0].opens == np.array([100, 200, 300])).all())
        self.assertTrue(
            (hd1[0].highs == np.array([1000, 2000, 3000])).all())
        self.assertTrue(
            (hd1[0].lows == np.array([1, 2, 3])).all())
        self.assertTrue(
            (hd1[1].closes == np.array([11, 21, 31])).all())
        self.assertTrue(
            (hd1[1].opens == np.array([110, 210, 310])).all())
        self.assertTrue(
            (hd1[1].highs == np.array([1100, 2100, 3100])).all())
        self.assertTrue(
            (hd1[1].lows == np.array([111, 211, 311])).all())


if __name__ == '__main__':
    unittest.main()
