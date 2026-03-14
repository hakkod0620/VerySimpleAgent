import yfinance as yf
import pandas as pd

# 1. 設定我們要抓取的股票代碼 (台積電在 Yahoo Finance 的代號是 2330.TW)
ticker_symbol = "AAPL" 
period="1y"
print(f"啟動連線！正在抓取 {ticker_symbol} 的資料...")

# 2. 建立一個 Ticker 物件來對接 Yahoo 財經資料庫
ticker_data = yf.Ticker(ticker_symbol)

# 3. 取得歷史股價資料
# 這裡的 period="1mo" 代表抓取過去「1個月」的資料
historical_data = ticker_data.history(period="1mo")

# 4. 使用 Pandas 的功能，印出資料的「前 5 行」來檢查
print("\n--- 資料抓取成功！以下是前 5 筆紀錄 ---")
print(historical_data.head())