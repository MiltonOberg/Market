import json

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
        df = self.stock.df

        json_table = df.to_html(classes="table table-striped table-bordered", border=0)
        return json_table

    def get_graph(self):
        fig = StockGraph(choice=self.stock)
        fig = fig.create_graph()
        return json.dumps(fig, cls=PlotlyJSONEncoder)
