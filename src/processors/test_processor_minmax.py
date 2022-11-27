import unittest
import datetime
import processor_minmax as prminmax
import marketdata
import numpy as np
from marketdata.utils import date_from_year


class MyTestCase(unittest.TestCase):
    def test_processor_minmax(self):
        processor = prminmax.ProcessorMinMax()

        hd = marketdata.HistoricData(
            "IBM", [date_from_year(2002), date_from_year(2003), date_from_year(2004), date_from_year(2005),
                    date_from_year(2006)], np.array([10, 20, 30, 15, 7]),
            np.array([100, 200, 300, 100, 100]), np.array([1000, 2000, 3000, 1000, 1000]), np.array([1, 2, 3, 3, 3]))

        self.assertEqual(processor.process(hd)['close_min'], 7)
        self.assertEqual(processor.process(hd)['date_min'], datetime.datetime(2006, 1, 1, 1, 1, 1))
        self.assertEqual(processor.process(hd)['close_max'], 30)
        self.assertEqual(processor.process(hd)['date_max'], datetime.datetime(2004, 1, 1, 1, 1, 1))


if __name__ == '__main__':
    unittest.main()
