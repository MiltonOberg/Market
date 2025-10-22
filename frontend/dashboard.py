import streamlit as st

from backend.features.predict_stock import PredictStock
from frontend.style.read_css import read_css
from frontend.ui.stock_analysis import StockAnalysis
from utils.period_options import PERIOD_MAP


def main():
    read_css()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(" Navigation", ["Home", "Stock Analysis", "AI Model"])
    if page == "Home":
        st.title("Hello World!")

    if page == "Stock Analysis":
        st.title("Stock Analysis")
        time = st.radio(
            "What time frame would you like to see?",
            [option for option in PERIOD_MAP.keys()],
            horizontal=True,
        )
        choice = st.text_input("What stonk do you want to analyse?", key="analysis")

        if choice and time:
            stonk_analysis = StockAnalysis(choice=choice, timeframe=PERIOD_MAP[time])
            stonk_analysis.show_table()
            stonk_analysis.show_graph()

    if page == "AI Model":
        st.title("AI Model")
        days = st.slider("Days to predict", min_value=0, max_value=30)
        choice = st.text_input("What stonk do you want to analyse?", key="ai")

        if choice:
            preds = PredictStock(choice=choice).predict_days(days=days)
            stock_analysis = StockAnalysis(choice=preds)
            stock_analysis.show_table()
            stock_analysis.show_graph()


if __name__ == "__main__":
    main()
