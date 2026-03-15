import yfinance as yf
import pandas as pd


ticker_symbol = "AAPL" 
period="1y"
print(f"！正在抓取 {ticker_symbol} 的資料...")
ticker_data = yf.Ticker(ticker_symbol)


historical_data = ticker_data.history(period="1mo")


print("\n--- 前 5 筆紀錄 ---")
print(historical_data.head())
