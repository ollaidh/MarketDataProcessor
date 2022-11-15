import matplotlib.pyplot as plt
import numpy as np


def draw_plot(dates, closes, opens=None, highs=None, lows=None):
    counter = 0
    plot_ticks = []
    for price in closes:
        counter += 1
        plot_ticks.append(counter)

    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_xlabel('Days')
    ax.set_ylabel('Open')
    ax.set_title('  Apple (AAPL) \n Historical Data')
    ax.grid(True)

    ax.plot(np.arange(len(closes)), closes, label='Close')
    if opens:
        ax.plot(np.arange(len(opens)), opens, label='Open')
    if highs:
        ax.plot(np.arange(len(highs)), highs, label='High')
    if lows:
        ax.plot(np.arange(len(lows)), lows, label='Low')

    ax.legend()

    # ax.set_xticks(np.arange(0, len(dates), 1), dates)

    plt.show()
