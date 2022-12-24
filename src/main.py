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
    except md.config.NoTicker as err:
        print(err)
        return
    except md.config.NoPeriod as err:
        print(err)
        return
    except md.config.NoInterval as err:
        print(err)
        return
    except md.config.NoPrice as err:
        print(err)
        return
    except md.config.NoProcessor as err:
        print(err)
        return

    data = md.import_historic_data(stock_parameters)
    # print(data)

    # execute processor, which is set in json:
    processors_available = {
        'minmax': processors.ProcessorMinMax,
        'percdelta': processors.ProcessorPercDelta,
        'percdeltaminmax': processors.ProcessorPercDeltaMinMax,
        'volatility': processors.ProcessorVolatility
    }

    for company in data:
        for pr in stock_parameters.processor['type']:
            process = processors_available[pr]()
            print(company.company, process.process(company))



    # prints on the plot:
    # stock_plot.draw_plot(dates, closes)
    # print(marketdata.config.load_config_ffile('stock_parameters.json'))
    # print(marketdata.config.load_config_fstring(json.dumps(marketdata.config.load_config_ffile('stock_parameters.json'))))

if __name__ == '__main__':
    main()


