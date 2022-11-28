import marketdata


class ProcessorPercDelta:
    def process(self, dataset: marketdata.HistoricData) -> dict:
        start_value = dataset.price[0]
        end_value = dataset.price[len(dataset.dates) - 1]
        delta_perc = 100 * abs(end_value - start_value) / start_value
        return {'delta_perc': delta_perc}
