import json

import numpy as np
import pandas as pd
from plotly.utils import PlotlyJSONEncoder

from backend.components.stock import Stock
from backend.components.stock_graph import StockGraph


class StockAnalysis:
    def __init__(
        self,
        choice: str = None,
        data: np.ndarray = None,
        timeframe: str = "2y",
        interval: str = "1d",
    ):
        self.choice = choice
        self.data = data
        self.timeframe = timeframe
        self.interval = interval
        self.stock = None
        if choice:
            self.stock = Stock(stock=choice, timeframe=timeframe, interval=interval)

    def get_table(self):
        df = self.stock.df if self.stock else pd.DataFrame(self.data)

        json_table = df.to_html(classes="table table-striped table-bordered", border=0)
        return json_table

    def get_graph(self):
        fig = StockGraph(choice=self.stock if self.stock else self.data)
        fig = fig.create_graph()
        return json.dumps(fig, cls=PlotlyJSONEncoder)
