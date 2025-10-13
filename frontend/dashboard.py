import streamlit as st

from frontend.ui.stock_analysis import StockAnalysis


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(" Navigation", ["Home", "Stock Analysis", "AI Model"])
    if page == "Home":
        st.title("Hello World!")

    if page == "Stonk Analysis":
        st.title("Stonk Analysis")
        choice = st.text_input("What stonk do you want to analyse?")
        if choice:
            stonk_analysis = StockAnalysis(choice=choice)
            stonk_analysis.show_table()
            stonk_analysis.show_graph()

    if page == "AI Model":
        st.title("AI Model")


if __name__ == "__main__":
    main()
