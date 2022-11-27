import numpy as np
import yfinance as yf
from dataclasses import dataclass
import datetime

from .config import Config


@dataclass(frozen=True)
class HistoricData:
    company: str
    dates: list[datetime.datetime]
    closes: np.array
    opens: np.array
    highs: np.array
    lows: np.array


def import_historic_data(config: Config) -> list:
    result = []
    companies = config.companies

    for company in companies:
        ticker = yf.Ticker(company)
        history = ticker.history(period=config.period, interval=config.interval)
        dates = history.index.to_pydatetime().tolist()
        closes = history['Close'].to_numpy()
        opens = history['Open'].to_numpy()
        highs = history['High'].to_numpy()
        lows = history['Low'].to_numpy()
        stock = HistoricData(company, dates, closes, opens, highs, lows)
        result.append(stock)

    return result


