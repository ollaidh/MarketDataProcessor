import unittest
import processors.processor_volatility as pv
import marketdata
import numpy as np
from marketdata.utils import date_from_years


class TestVolatility(unittest.TestCase):
    def test_processor_volatility(self):
        processor = pv.ProcessorVolatility()

        hd1 = marketdata.HistoricData(
            "IBM", date_from_years([2002, 2003, 2004, 2005, 2006]), np.array([10, 20, 30, 15, 7]))
        hd2 = marketdata.HistoricData(
            "AAPL", date_from_years([2002, 2003, 2004, 2005, 2006, 2007]), np.array([72, 20, 35, 15, 10, 3]))
        hd3 = marketdata.HistoricData(
            "AAPL", date_from_years([2002, 2003, 2004]), np.array([100, 20, 30]))

        self.assertEqual(round(processor.process(hd1)['volatility']), 18)
        self.assertEqual(round(processor.process(hd2)['volatility']), 56)
        self.assertEqual(round(processor.process(hd3)['volatility']), 62)

if __name__ == '__main__':
    unittest.main()
