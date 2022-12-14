import unittest
import datetime
import processors.processor_minmax as prminmax
import marketdata
import numpy as np
from marketdata.utils import date_from_years


class MyTestCase(unittest.TestCase):
    def test_processor_minmax(self):
        processor = prminmax.ProcessorMinMax()

        hd = marketdata.HistoricData(
            "IBM", date_from_years([2002, 2003, 2004, 2005, 2006]), np.array([10, 20, 30, 15, 7])
        )

        self.assertEqual(processor.process(hd)['close_min'], 7)
        self.assertEqual(processor.process(hd)['date_min'], datetime.datetime(2006, 1, 1, 1, 1, 1))
        self.assertEqual(processor.process(hd)['close_max'], 30)
        self.assertEqual(processor.process(hd)['date_max'], datetime.datetime(2004, 1, 1, 1, 1, 1))


if __name__ == '__main__':
    unittest.main()
