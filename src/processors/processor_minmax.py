import numpy as np
import marketdata


class ProcessorMinMax:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        historicdata_min = np.argmin(dataset.closes)
        historicdata_max = np.argmax(dataset.closes)
        return {'close_min': dataset.closes[historicdata_min], 'date_min': dataset.dates[historicdata_min],
                'close_max': dataset.closes[historicdata_max], 'date_max': dataset.dates[historicdata_max]}


