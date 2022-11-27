import marketdata


class ProcessorPercDelta:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        start_value = dataset.closes[0]
        end_value = dataset.closes[len(dataset.dates) - 1]
        delta_perc = 100 * abs(end_value - start_value) / start_value
        return {'delta_perc': delta_perc}
