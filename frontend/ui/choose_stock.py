import streamlit as st
from ui.components.button import button

from backend.components.stock import Stock
from backend.components.stock_graph import StockGraph


class StockAnalysis:
    def __init__(self, choice: str):
        self.choice = choice

    def show_table(self):
        stonk = Stock(self.choice)
        if stonk:
            st.dataframe(stonk.df)

    def show_graph(self):
        stonk_graph = StockGraph(self.choice)
        button("Graph", stonk_graph.date_close, "date_close")
