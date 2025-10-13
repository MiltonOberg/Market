import numpy as np
import pandas as pd
import plotly.express as px

from backend.components.stock import Stock


class StockGraph:
    def __init__(self, choice: str):
        if isinstance(choice, str):
            self.df = Stock(choice).df
        elif isinstance(choice, Stock):
            self.df = choice.df
        elif isinstance(choice, np.ndarray):
            self.df = pd.DataFrame(choice, columns=["Close"])

    def date_close(self, year: int = None, month: int = None):
        df_copy = self.df.copy()
        if year is not None or month is not None:
            if year is not None:
                df_copy = self.df[self.df.index.year == year]
            if month is not None:
                df_copy = self.df[self.df.index.month == month]
        else:
            df_copy = self.df

        fig = px.line(df_copy, x=df_copy.index, y="Close", title="Stonk Closing Prices")
        return fig
