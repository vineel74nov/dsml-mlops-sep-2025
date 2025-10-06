import streamlit as st
import pandas as pd
import numpy as np

#pip install yfinance

import yfinance as yf
from curl_cffi import requests
session = requests.Session(impersonate="chrome")



st.title('Stock Market Data Analysis')

# Header
#st.header("This is a header")
 
## Subheader
#st.subheader("This is a subheader")

#st.write("# Welcome to Streamlit! 👋")

#ticker_symbol = 'AAPL'  # Default ticker symbol
ticker_symbol = st.text_input("Please enter Ticker Symbol", 'AAPL')

ticker_data = yf.Ticker(ticker_symbol, session=session)

import datetime

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 10, 10)

ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

st.dataframe(ticker_df)