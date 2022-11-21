import numpy as np
import yfinance as yf
import pandas as pd
from dataclasses import dataclass

from .config import Config


@dataclass(frozen=True)
class HistoricData:
    dates: list[pd.Timestamp]
    closes: np.array
    opens: np.array
    highs: np.array
    lows: np.array


def import_historic_data(config: Config) -> HistoricData:
    ticker = yf.Ticker(config.company)

    history = ticker.history(period=config.period, interval=config.interval)

    dates = history.index.tolist()

    closes = history['Close'].to_numpy()
    opens = history['Open'].to_numpy()
    highs = history['High'].to_numpy()
    lows = history['Low'].to_numpy()

    stock = HistoricData(dates, closes, opens, highs, lows)

    return stock


