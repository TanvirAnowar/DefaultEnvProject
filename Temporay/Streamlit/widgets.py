import streamlit as st
import pandas as pd

st.title('Text input')

name = st.text_input('Enter your name')

age = st.slider('Enter your age',0,100,25)

if name:
    st.write('Hello', name)
    
options = ['red', 'blue', 'green']

choice = st.selectbox('Choose a color', options)

st.write('Hello', name, 'your age is', age)

file_upload = st.file_uploader('Upload a file', type='csv')

if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.write(df)
    