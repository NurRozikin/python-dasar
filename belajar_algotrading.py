from streamlit.proto.Heading_pb2 import Heading
import yfinance as yf
import pandas_ta as ta
import pandas as pd
import pytz
from datetime import datetime as dt
import streamlit as st
import plotly.graph_objs as go

def get_ticker_data(ticker_symbol, data_period, data_interval) :
    ticker_data = yf.download(tickers=ticker_symbol, period=data_period, interval=data_interval)
    if len(ticker_data) == 0:
        st.info("Could not find the ticker data. Modify ticker symbol or reduce the period value")
    else:
        ticker_data.index  = ticker_data.index.strftime('%d-%m-%Y %H:%M')
    return ticker_data

def plot_candle_chart(ticker_data):
    candle_fig = go.Figure()
    candle_fig.add_trace(go.Candlestick(x=ticker_data.index, 
                                        open=ticker_data['Open'], 
                                        close=ticker_data['Close'],
                                        low=ticker_data['Low'],
                                        high=ticker_data['High'],
                                        name='Market Data'))
    candle_fig.update_layout(height=800)
    st.write(candle_fig)

def initAlgo() :
  print("init algo trading")
  '''
    
  tz = pytz.timezone("Asia/Bangkok")
  start = tz.localize(dt(2024,1,1))
  end = tz.localize(dt.today())
  
  df = yf.download("AAPL", start, end)

  new_names = {
      'ISA_9': 'tenkan_sen', 
      'ISB_26': 'kijun_sen', 
      'ITS_9': 'senkou_span_a', 
      'IKS_26': 'senkou_span_b', 
      'ICS_26': 'chikou_span'
  }
  
  ich = ta.ichimoku(df["High"], df["Low"], df["Close"],senkou=True)[0].rename(columns=new_names)
  df=pd.concat([df,ich],axis=1)

  print(df)
  '''
  ticker_symbol = st.sidebar.text_input("Ticker Symbol", "AAPL")
  data_period = st.sidebar.text_input("Period", "1mo")
  data_interval = st.sidebar.radio("Interval", ['1d', '5d', '1mo'])

  st.header(ticker_symbol)
  ticker_data = get_ticker_data(ticker_symbol, data_period, data_interval)
  plot_candle_chart(ticker_data)
