import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np




st.title("Stock Market Analysis!!")

ticker_symbol = 'AAPL'

ticker_data = yf.Ticker(ticker_symbol)

import datetime

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 10, 10)

ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

st.dataframe(ticker_df)