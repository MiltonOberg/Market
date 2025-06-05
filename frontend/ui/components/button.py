import streamlit as st


def button(label: str, function: callable, key: str):
    if key not in st.session_state:
        st.session_state[key] = False

    if st.button(label=label):
        st.session_state[key] = not st.session_state[key]

    if st.session_state[key]:
        st.plotly_chart(function())
