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
import altair as alt

#start_date = datetime.date(2024, 1, 1)
#end_date = datetime.date(2024, 10, 10)
col1, col2 = st.columns(2)

with col1:
	start_date = st.date_input("Please enter Starting Date",
				  datetime.date(2019,1,1))

with col2:
	end_date = st.date_input("Please enter End Date",
				  datetime.date(2022,12,31))
	
if start_date < datetime.date(2010,1,1):
	st.warning("Start date should be after 2010-01-01")
if end_date > datetime.date.today():
	st.warning("End date should not be in the future")


ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

st.dataframe(ticker_df)

st.write("## Closing price of " + ticker_symbol)
st.line_chart(ticker_df['Close'])

st.write("## Volume price of " + ticker_symbol)
st.line_chart(ticker_df['Volume'])

col1, col2 = st.columns(2)

with col1:
	st.write("## Opening price of " + ticker_symbol)
	st.line_chart(ticker_df['Open'])

with col2:
	st.write("## High price of " + ticker_symbol)
	st.line_chart(ticker_df['High'])


# Exponential Moving Average
st.write("## Exponential Moving Average")

alpha = st.slider("Select Alpha value for EMA", min_value=0.01, max_value=1.0, value=0.1, step=0.01)

# Calculate EMA
ema_values = []
ema = ticker_df['Close'].iloc[0]  # Initialize with first closing price
ema_values.append(ema)

for i in range(1, len(ticker_df)):
	ema = alpha * ticker_df['Close'].iloc[i] + (1 - alpha) * ema
	ema_values.append(ema)

ticker_df['EMA'] = ema_values

# Plot closing price with EMA using custom colors

chart_data = ticker_df[['Close', 'EMA']].reset_index()
chart_data_melted = chart_data.melt('Date', var_name='Type', value_name='Price')

chart = alt.Chart(chart_data_melted).mark_line().add_selection(
	alt.selection_interval()
).encode(
	x='Date:T',
	y='Price:Q',
	color=alt.Color('Type:N', scale=alt.Scale(domain=['Close', 'EMA'], range=['blue', 'red']))
).resolve_scale(
	color='independent'
)

st.altair_chart(chart, use_container_width=True)



num = st.number_input('Insert a number')

if(st.button("Calculate Square")):
	result = num ** 2
	st.text("Square of " + str(num) + " is " + str(result))