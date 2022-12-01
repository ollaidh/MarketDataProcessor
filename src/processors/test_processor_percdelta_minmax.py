import unittest
import processors.processor_percdelta_minmax as ppdmm
import marketdata
import numpy as np
from marketdata.utils import date_from_years


class MyTestCase(unittest.TestCase):
    def test_processor_percdelta_minmax(self):
        processor = ppdmm.ProcessorPercDeltaMinMax()

        hd1 = marketdata.HistoricData(
            "IBM", date_from_years([2002, 2003, 2004, 2005, 2006]), np.array([160, 200, 180, 185, 150]))
        hd2 = marketdata.HistoricData(
            "AAPL", date_from_years([2002, 2003, 2004, 2005, 2006]), np.array([7, 8, 14, 9, 7]))
        hd3 = marketdata.HistoricData(
            "AAPL", date_from_years([2002, 2003, 2004, 2005, 2006]), np.array([100, 20, 30, 15, 5]))

        self.assertEqual(round(processor.process(hd1)['deltaperc_minmax'], 1), 33.3)
        self.assertEqual(round(processor.process(hd2)['deltaperc_minmax'], 1), 100)
        self.assertEqual(round(processor.process(hd3)['deltaperc_minmax'], 1), 1900)


if __name__ == '__main__':
    unittest.main()
