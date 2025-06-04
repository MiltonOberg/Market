import streamlit as st
from backend.features.stonk import Stonk
from backend.features.stonk_graph import StonkGraph


class ChooseStonk:
    def show_data(self):

        choice = st.text_input(  "What stonk do you want to analyse?")
        if choice:
            stonk = Stonk(choice)
            stonk_graph = StonkGraph(choice)

            if stonk:
                st.dataframe(stonk.df)

            if "show_graph" not in st.session_state:
                st.session_state.show_graph = False

            if st.button("Graph"):
                st.session_state.show_graph = not st.session_state.show_graph

            if st.session_state.show_graph:
                st.plotly_chart(stonk_graph.date_close())
