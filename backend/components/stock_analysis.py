import json

import pandas as pd
from plotly.utils import PlotlyJSONEncoder

from backend.components.stock import Stock
from backend.components.stock_graph import StockGraph


class StockAnalysis:
    def __init__(
        self,
        choice: str,
        timeframe: str = "2y",
        interval: str = "1d",
    ):
        self.choice = choice
        self.timeframe = timeframe
        self.interval = interval
        self.stock = Stock(stock=choice, timeframe=timeframe, interval=interval)

    def get_table(self):
        df = pd.DataFrame(self.stock.df, columns=["Close"])
        return df

    def get_graph(self):
        fig = StockGraph(choice=self.stock)
        fig = fig.create_graph()
        return json.dumps(fig, cls=PlotlyJSONEncoder)
