import numpy as np
import yfinance as yf
from dataclasses import dataclass
import datetime

from .config import Config


@dataclass(frozen=True)
class HistoricData:
    company: str
    dates: list[datetime.datetime]
    price: np.array


def import_historic_data(config: Config) -> list:
    result = []
    companies = config.companies

    for company in companies:
        ticker = yf.Ticker(company)
        history = ticker.history(period=config.period, interval=config.interval)
        dates = history.index.to_pydatetime().tolist()
        if config.price == 'close':
            price = history['Close'].to_numpy()
        elif config.price == 'open':
            price = history['Open'].to_numpy()
        elif config.price == 'high':
            price = history['High'].to_numpy()
        elif config.price == 'low':
            price = history['Low'].to_numpy()
        else:
            raise KeyError(f'Unknown price format: {config.price}')
        stock = HistoricData(company, dates, price)
        result.append(stock)

    return result


