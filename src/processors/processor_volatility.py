import math
import numpy as np
import marketdata


class ProcessorVolatility:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        std_dev = np.std(dataset.price)
        days = len(dataset.price)
        volatility = std_dev * math.sqrt(days)
        return {'volatility': volatility}
