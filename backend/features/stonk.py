import yfinance as yf
from yahooquery import search


class Stonk:
    def __init__(self, stonk: str):
        self.df = self._get_data(stonk)

    def _get_symbol(self, stonk: str):
        result = search(stonk)
        return result["quotes"][1]["symbol"]

    def _get_data(self, stonk: str, period: str = "2y", interval: str = "1d"):
        symbol = self._get_symbol(stonk)
        data = yf.Ticker(symbol)
        self.df = data.history(period=period, interval=interval)
