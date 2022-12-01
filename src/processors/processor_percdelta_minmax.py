import marketdata
import numpy as np


class ProcessorPercDeltaMinMax:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        historicdata_min = np.argmin(dataset.price)  # index of min value
        historicdata_max = np.argmax(dataset.price)  # index of max value
        deltaperc_minmax = 100 * abs(dataset.price[historicdata_max] - dataset.price[historicdata_min]) / dataset.price[historicdata_min]
        return {'deltaperc_minmax': deltaperc_minmax}
