import streamlit as st

from backend.features.predict_stock import PredictStock
from frontend.ui.stock_analysis import StockAnalysis


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(" Navigation", ["Home", "Stock Analysis", "AI Model"])
    if page == "Home":
        st.title("Hello World!")

    if page == "Stock Analysis":
        st.title("Stock Analysis")
        choice = st.text_input("What stonk do you want to analyse?", value="")
        if choice:
            stonk_analysis = StockAnalysis(choice=choice)
            stonk_analysis.show_table()
            stonk_analysis.show_graph()

    if page == "AI Model":
        st.title("AI Model")
        days = st.slider("Days to predict", min_value=1, max_value=30)
        choice = st.text_input("What stonk do you want to analyse?", value="")

        if choice:
            preds = PredictStock(choice=choice).predict_days(days=days)
            stock_analysis = StockAnalysis(choice=preds)
            stock_analysis.show_table()
            stock_analysis.show_graph()


if __name__ == "__main__":
    main()
