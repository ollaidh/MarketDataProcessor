import sys

import stock_data
import config
import cmdline_parser
import json
import stock_plot


if __name__ == '__main__':
    args = cmdline_parser.parse(sys.argv[1:])
    stock_parameters = config.load_config_ffile(args.config)
    data = stock_data.import_history(stock_parameters)
    print(data)
    # stock_plot.draw_plot(dates, closes)

    # print(config.load_config_ffile('stock_parameters.json'))
    # print(config.load_config_fstring(json.dumps(config.load_config_ffile('stock_parameters.json'))))

