import yfinance as yf
from yahooquery import search


class Stonk:
    def __init__(self, stonk: str):
        self.df = self._get_data(stonk)

    def _get_symbol(self, stonk: str):
        try:
            result = search(stonk)
            return result["quotes"][1]["symbol"]
        except Exception as e:
            raise ValueError(f"Error fetching data for {stonk}: {e}")

    def _get_data(self, stonk: str, period: str = "2y", interval: str = "1d"):
        symbol = self._get_symbol(stonk)
        try:
            data = yf.Ticker(symbol)
            return data.history(period=period, interval=interval)[::-1]
        except Exception as e:
            raise ValueError(f"Error fetching data for {stonk}: {e}")
