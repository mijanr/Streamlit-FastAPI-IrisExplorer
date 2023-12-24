"""
Show the raw dataset
"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import requests

# get the head data from fastapi endpoint /iris
url = "http://localhost:8000/iris"
r = requests.get(url)
df = pd.DataFrame(r.json())

# Display options
display_options = st.sidebar.selectbox("Display Options", ["Head", "Tail"])

if display_options == "Head":
    # display the head
    st.title("Iris dataset head")
    st.write(df.head())
else:
    # display the tail
    st.title("Iris dataset tail")
    st.write(df.tail())

# Show the entire dataset
if st.sidebar.checkbox("Show entire dataset"):
    # display the entire dataset
    st.title("Iris dataset")
    st.write(df)

# show summary statistics and info
if st.sidebar.checkbox("Show summary statistics and info"):
    # describe
    st.title("Summary statistics")
    st.write(df.describe())

    # df.info 
    st.title("Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

