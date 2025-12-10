from pathlib import Path

import streamlit as st


def read_css():
    css_path = Path(__file__).parent / "style.css"

    with open(css_path) as css:
        st.markdown(f"<style>{css.read()}<style>", unsafe_allow_html=True)
