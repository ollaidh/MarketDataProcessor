import unittest
import processor_percdelta as ppd
import marketdata
import numpy as np
from marketdata.utils import date_from_year


class MyTestCase(unittest.TestCase):
    def test_processor_percdelta(self):
        processor = ppd.ProcessorPercDelta()

        hd1 = marketdata.HistoricData(
            "IBM", [date_from_year(2002), date_from_year(2003), date_from_year(2004), date_from_year(2005),
                    date_from_year(2006)], np.array([10, 20, 30, 15, 7]))
        hd2 = marketdata.HistoricData(
            "AAPL", [date_from_year(2002), date_from_year(2003), date_from_year(2004), date_from_year(2005),
                     date_from_year(2006)], np.array([7, 20, 30, 15, 10]))
        hd3 = marketdata.HistoricData(
            "AAPL", [date_from_year(2002), date_from_year(2003), date_from_year(2004), date_from_year(2005),
                     date_from_year(2006)], np.array([100, 20, 30, 15, 7]))

        self.assertEqual(processor.process(hd1)['delta_perc'], 30)
        self.assertEqual(round(processor.process(hd2)['delta_perc'], 1), 42.9)
        self.assertEqual(processor.process(hd3)['delta_perc'], 93)


if __name__ == '__main__':
    unittest.main()
