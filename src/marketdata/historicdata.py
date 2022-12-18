import numpy as np
import yfinance as yf
from dataclasses import dataclass
import datetime
import pandas as pd
import json

from .config import Config


class InputSizeNotEqualError(Exception):
    def __str__(self):
        return 'Dates and prices arrays have different size!'


@dataclass(frozen=True)
class HistoricData:
    company: str
    dates: list[datetime.datetime]
    price: np.array

    def __post_init__(self):
        if len(self.dates) != self.price.size:
            raise InputSizeNotEqualError


def calc_average_price(history: pd.DataFrame, price_types: list) -> np.array:
    mapping = {'close': 'Close', 'open': 'Open', 'high': 'High', 'low': 'Low'}
    prices = []
    for item in price_types:
        key = mapping[item]
        curr_price = history[key].to_numpy()
        prices.append(curr_price)

    result = np.mean(prices, axis=0)
    return result


def import_historic_data(config: Config) -> list:
    result = []
    for company in config.tickers:
        ticker = yf.Ticker(company)
        if config.period is not None:
            history = ticker.history(period=config.period, interval=config.interval)
        else:
            history = ticker.history(start=config.start_date, end=config.end_date, interval=config.interval)
        dates = history.index.to_pydatetime().tolist()
        price = calc_average_price(history, config.price)
        stock = HistoricData(company, dates, price)
        result.append(stock)

    return result


