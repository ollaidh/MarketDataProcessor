import numpy as np
import marketdata


class ProcessorMinMax:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        historicdata_min = np.argmin(dataset.price)
        historicdata_max = np.argmax(dataset.price)
        return {'close_min': dataset.price[historicdata_min], 'date_min': dataset.dates[historicdata_min],
                'close_max': dataset.price[historicdata_max], 'date_max': dataset.dates[historicdata_max]}


