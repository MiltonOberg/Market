import plotly.express as px

from backend.features.stonk import Stonk


class StonkGraph:
    def __init__(self, stonk: str):
        self.df = Stonk(stonk).df

    def date_close(self):
        fig = px.line(self.df, x=self.df.index, y="Close", title="Stonk Closing Prices")
        return fig
