import yfinance as yf
from yahooquery import search


class Stock:
    def __init__(self, stock: str):
        self.df = self._get_data(stock)

    def _get_symbol(self, stock: str):
        try:
            result = search(stock)
            return result["quotes"][0]["symbol"]
        except Exception as e:
            raise ValueError(f"Error fetching data for {stock}: {e}")

    def _get_data(self, stock: str, period: str = "2y", interval: str = "1d"):
        symbol = self._get_symbol(stock)
        try:
            data = yf.Ticker(symbol)
            return data.history(period=period, interval=interval)
        except Exception as e:
            raise ValueError(f"Error fetching data for {stock}: {e}")
