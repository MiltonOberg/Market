import yfinance as yf


class Market:
    def __init__(self):
        self.df = None

    def get_data(self, stonk):
        data = yf.Ticker(f"{stonk}")
        self.df = data.history(period="2y", interval="1d")
