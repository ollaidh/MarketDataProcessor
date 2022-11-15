import numpy as np
import yfinance as yf
from dataclasses import dataclass


@dataclass(frozen=True)
class HistoricData:
    dates: []
    closes: np.array([])
    opens: np.array([])
    highs: np.array([])
    lows: np.array([])


def import_history(config):
    ticker = yf.Ticker(config.company)

    history = ticker.history(period=config.period, interval=config.interval)

    dates = history.index.tolist()

    closes = history['Close'].to_numpy()
    opens = history['Open'].to_numpy()
    highs = history['High'].to_numpy()
    lows = history['Low'].to_numpy()

    stock = HistoricData(dates, closes, opens, highs, lows)

    return stock
