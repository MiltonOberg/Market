import streamlit as st
from ui.choose_stonk import ChooseStonk


def main():
    st.title("Hello World!")
    st.sidebar.title("Navigation")
    ChooseStonk().show_data()


if __name__ == "__main__":
    main()
