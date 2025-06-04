import streamlit as st
from ui.choose_stonk import StonkAnalysis


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(" Navigation", ["Home", "Stonk Analysis"])
    if page == "Home":
        st.title("Hello World!")

    if page == "Stonk Analysis":
        st.title("Stonk Analysis")
        choice = st.text_input("What stonk do you want to analyse?")
        if choice:
            stonk_analysis = StonkAnalysis(choice=choice)
            stonk_analysis.show_table()
            stonk_analysis.show_graph()


if __name__ == "__main__":
    main()
