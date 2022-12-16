import math
import numpy as np
import marketdata


class ProcessorVolatility:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        std_dev = np.std(dataset.price)
        volatility = std_dev * math.sqrt(252)  # assume one year has 252 business days and we calc volatility per year
        return {'volatility': volatility}
