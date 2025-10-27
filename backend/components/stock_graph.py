import numpy as np
import pandas as pd
import plotly.graph_objects as go

from backend.components.stock import Stock


class StockGraph:
    def __init__(self, choice: Stock | np.ndarray | str):
        self.df = None
        if isinstance(choice, str):
            self.df = Stock(stock=choice).df
        elif isinstance(choice, Stock):
            self.df = choice.df
        elif isinstance(choice, np.ndarray):
            self.df = pd.DataFrame(choice, columns=["Close"])

    def create_graph(self):
        data = go.Scatter(
            x=self.df.index.tolist(),
            y=self.df["Close"].values.tolist(),
            mode="lines",
            name="Close Price",
        )
        fig = go.Figure(data=data)
        return fig
