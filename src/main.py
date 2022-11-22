import sys

import cmdline_parser
import marketdata

import stock_plot
import json


if __name__ == '__main__':
    args = cmdline_parser.parse(sys.argv[1:])
    stock_parameters = marketdata.load_config_ffile(args.config)
    data = marketdata.import_historic_data(stock_parameters)
    print(data)

    # prints on the plot:
    # stock_plot.draw_plot(dates, closes)
    # print(marketdata.config.load_config_ffile('stock_parameters.json'))
    # print(marketdata.config.load_config_fstring(json.dumps(marketdata.config.load_config_ffile('stock_parameters.json'))))

