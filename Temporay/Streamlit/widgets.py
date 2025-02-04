import streamlit as st

st.title('Text input')

name = st.text_input('Enter your name')

if name:
    st.write('Hello', name)
