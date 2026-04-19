import yfinance as yf
from yahooquery import search


class Stock:
    def __init__(
        self, stock: str = "saab", timeframe: str = "max", interval: str = "1d"
    ):
        self.timeframe = timeframe
        self.interval = interval
        self.df = self._get_data(stock)

    def _get_symbol(self, stock: str):
        try:
            result = search(stock)
            return result["quotes"][0]["symbol"]
        except Exception as e:
            raise ValueError(f"Error fetching data for {stock}: {e}")

    def _get_data(self, stock: str):
        symbol = self._get_symbol(stock)
        try:
            data = yf.Ticker(symbol)
            return data.history(period=self.timeframe, interval=self.interval)
        except Exception as e:
            raise ValueError(f"Error fetching data for {stock}: {e}")

    def get_return_data(self):
        df = self.df.copy()
        df["Return"] = df["Close"].pct_change()
        df.dropna(inplace=True)
        return df


if __name__ == "__main__":
    stock = Stock("saab")
    print(stock.get_return_data())
