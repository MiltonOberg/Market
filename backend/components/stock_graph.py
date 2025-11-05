import numpy as np
import pandas as pd
import plotly.graph_objects as go

from backend.components.stock import Stock
from frontend.style.colors_py import COLORS


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
        fig.update_layout(
            title="Stock price over time",
            paper_bgcolor=COLORS["light_navy"],
            font=dict(color=COLORS["white"]),
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False),
        )
        return fig
