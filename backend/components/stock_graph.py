import plotly.express as px

from backend.components.stock import Stock


class StockGraph:
    def __init__(self, stonk: str):
        self.df = Stock(stonk).df

    def date_close(self, year: int = None, month: int = None):
        if year is not None or month is not None:
            if year is not None:
                self.df = self.df[self.df.index.year == year]
            if month is not None:
                self.df = self.df[self.df.index.month == month]

        fig = px.line(self.df, x=self.df.index, y="Close", title="Stonk Closing Prices")
        return fig
