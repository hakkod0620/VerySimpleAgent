import pandas as pd

print("啟動 Steam 數據分析模組...\n")

# 1. 讀取 CSV 檔案
# 提示：使用 pd.read_csv() 函數，括號裡面放入檔名字串
df = pd.read_csv("steam_games.csv")

# 2. 印出所有的資料
print("--- 原始資料 ---")
print(df)

# 3. 觀察資料的「健康狀況」(檢查缺失值與資料型態)
print("\n--- 資料表基本資訊 (Info) ---")
# 提示：使用 df.info() 可以看透這個資料表有幾個欄位、哪些欄位有空值
df.info()

import numpy as np # 我們需要 numpy 來呼叫真正的空值 (np.nan)

print("\n--- 啟動資料清洗手術 (升級版) ---")

# 1. 暴力破解法：強制把所有疑似數字的欄位轉成數值
# 只要遇到不是數字的垃圾字元 (例如 '      x  ')，errors='coerce' 會自動把它們變成 NaN
df['AppID'] = pd.to_numeric(df['AppID'], errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['NegativeReviews'] = pd.to_numeric(df['NegativeReviews'], errors='coerce')

# 2. 處理缺失值：現在垃圾字元都變成 NaN 了，我們安心地把評價的 NaN 補成 0
df['PositiveReviews'] = df['PositiveReviews'].fillna(0)
df['NegativeReviews'] = df['NegativeReviews'].fillna(0)

# 順便把 AppID 的空值也處理一下 (給它一個預設編號 0)
df['AppID'] = df['AppID'].fillna(0)

print("--- 清洗後的資料 ---")
print(df)
print("\n--- 清洗後的資料表基本資訊 (Info) ---")
df.info()








