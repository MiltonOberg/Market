import streamlit as st
from ui.componants.button import button

from backend.features.stonk import Stonk
from backend.features.stonk_graph import StonkGraph


class StonkAnalysis:
    def __init__(self, choice: str):
        self.choice = choice

    def show_table(self):
        stonk = Stonk(self.choice)
        if stonk:
            st.dataframe(stonk.df)

    def show_graph(self):
        stonk_graph = StonkGraph(self.choice)
        button("Graph", stonk_graph.date_close, "date_close")
