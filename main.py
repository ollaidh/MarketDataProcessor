import stock_data
import config
import json
import stock_plot


if __name__ == '__main__':
    stock_parameters = config.load_config_ffile('stock_parameters.json')
    data = stock_data.import_history(stock_parameters)
    # print(data)
    # stock_plot.draw_plot(dates, closes)

    # print(config.load_config_ffile('stock_parameters.json'))
    # print(config.load_config_fstring(json.dumps(config.load_config_ffile('stock_parameters.json'))))

