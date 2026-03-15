這是一個資料科學初學者的微型練習專案。
主要目的是透過實作，了解如何將基礎的資料處理、簡單的機器學習模型與大型語言模型結合，打造一個能透過自然語言進行基礎數據查詢的 AI Agent。

目前的資料集為手動建立的微型測試資料，用於驗證程式碼與 LangChain 框架的運作邏輯。

##  學習與實作重點

1. 基礎資料清理 (Data Cleaning)：
    練習使用 Pandas 處理空白字元、填補缺失值，確保資料型態。
    實作簡單的特徵工程。
2. 機器學習初探 (Machine Learning)：
   使用 Scikit-Learn 建立一個基礎的決策樹分類器 。
   定義目標變數，並觀察模型如何從特徵中學習簡單的分類規則。
3. LLM 整合 AI Agent：
   用LangChain 框架與 Google Gemini 2.5 Flash API 串接。
   測試 `create_pandas_dataframe_agent` 功能，觀察大語言模型如何將自然語言轉化為 Pandas 語法並輸出結果。

 用到的工具🛠️ 

Python
Pandas, NumPy
Scikit-Learn( DecisionTree )
LangChain, LangChain-Experimental

啟動

1. 安裝依賴：
   ```bash
   pip install pandas numpy scikit-learn langchain langchain-google-genai langchain-experimental python-dotenv tabulate
