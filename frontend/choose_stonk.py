import streamlit as st
from backend.features.stonk import Stonk


class ChooseStonk:
    def show_data(self):
        choice = st.text_input("What stonk do you want to analyse?")
        stonk = Stonk(choice)
        st.dataframe(stonk.df)
