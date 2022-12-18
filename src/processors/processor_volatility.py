import math
import numpy as np
import marketdata


class ProcessorVolatility:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        std_dev = np.std(dataset.price)
        volatility = std_dev * math.sqrt(252)  # TODO: REPLACE 252 WITH REAL NUMBER OF DAYS!!!
        return {'volatility': volatility}
