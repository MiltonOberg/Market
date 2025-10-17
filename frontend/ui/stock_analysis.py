import numpy as np
import pandas as pd
import streamlit as st
from ui.components.button import button

from backend.components.stock import Stock
from backend.components.stock_graph import StockGraph


class StockAnalysis:
    def __init__(self, choice: str, timeframe=None):
        self.choice = choice
        self.timeframe = timeframe

    def show_table(self):
        df = None
        if isinstance(self.choice, str):
            df = Stock(self.choice, timeframe=self.timeframe).df
        if isinstance(self.choice, Stock):
            df = self.choice.df
        if isinstance(self.choice, np.ndarray):
            df = pd.DataFrame(self.choice, columns=["Close"])
        st.dataframe(df[::-1])

    def show_graph(self):
        stonk_graph = StockGraph(self.choice)
        button("Graph", stonk_graph.date_close, "date_close")
