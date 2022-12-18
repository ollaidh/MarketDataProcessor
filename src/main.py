import sys

import cmdline_parser
import marketdata as md
import processors

def main():
    args = cmdline_parser.parse(sys.argv[1:])
    try:
        stock_parameters = md.load_config_ffile(args.config)
    except md.config.InvalidPeriodParameters as err:
        print(err)
        return

    data = md.import_historic_data(stock_parameters)
    # print(data)

    for company in data:
        if stock_parameters.processor == 'minmax':
            process = processors.ProcessorMinMax()
            print(process.process(company))
        elif stock_parameters.processor == 'percdelta':
            process = processors.ProcessorPercDelta()
            print(process.process(company))
        elif stock_parameters.processor == 'percdeltaminmax':
            process = processors.ProcessorPercDeltaMinMax()
            print(process.process(company))
        elif stock_parameters.processor['type'] == 'volatility':
            process = processors.ProcessorVolatility()
            print(process.process(company))

    # prints on the plot:
    # stock_plot.draw_plot(dates, closes)
    # print(marketdata.config.load_config_ffile('stock_parameters.json'))
    # print(marketdata.config.load_config_fstring(json.dumps(marketdata.config.load_config_ffile('stock_parameters.json'))))

if __name__ == '__main__':
    main()


