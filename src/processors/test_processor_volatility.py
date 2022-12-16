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
            "AAPL", date_from_years([2002, 2003, 2004, 2005, 2006]), np.array([72, 20, 35, 15, 10]))
        hd3 = marketdata.HistoricData(
            "AAPL", date_from_years([2002, 2003, 2004, 2005, 2006]), np.array([100, 20, 30, 15, 7]))

        self.assertEqual(round(processor.process(hd1)['volatility']), 129)
        self.assertEqual(round(processor.process(hd2)['volatility']), 356)
        self.assertEqual(round(processor.process(hd3)['volatility']), 534)

if __name__ == '__main__':
    unittest.main()
