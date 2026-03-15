import pandas as pd
import numpy as np

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




print("\n--- 進行特徵工程 (Feature Engineering) ---")

# 1. 計算「總評論數」
# 邏輯：總評論數 = 好評數 + 負評數
df['TotalReviews'] = df['PositiveReviews'] + df['NegativeReviews']

# 2. 計算「好評率」
# 邏輯：好評率 = 好評數 / 總評論數 (我們把它轉成百分比，所以乘以 100)
# 提示：請模仿上面的寫法，完成下面這行程式碼
df['PositiveRatio'] = (df['PositiveReviews'] / df['TotalReviews']) * 100

print("--- 最終準備餵給 AI 的精華資料 ---")
# 我們只挑選出未來要給 AI 訓練的「數值」欄位來看
print(df[['Name', 'Price', 'TotalReviews', 'PositiveRatio']])



print("\n--- 機器學習前置準備：建立預測目標 (Label) ---")

# 如果好評率 >= 90，標記為 1 (神作)，否則標記為 0 (普通)
# 提示：我們使用 np.where(條件, 符合時的值, 不符合時的值)
df['Is_Hit'] = np.where(df['PositiveRatio'] >= 90, 1, 0)

print(df[['Name', 'PositiveRatio', 'Is_Hit']])


print("\n--- 準備機器學習資料集 ---")

# 1. 將所有含有 NaN 的列刪除 (因為 sklearn 模型不接受空值)
# 提示：使用 dropna() 函數
df_ml = df.dropna()

# 2. 定義特徵 (X) 和目標 (y)
# X (Features): 模型用來學習的線索。我們選用 'Price' 和 'TotalReviews'
X = df_ml[['Price', 'TotalReviews']]

# y (Label/Target): 模型要預測的目標
y = df_ml['Is_Hit']

print("特徵 (X) 長這樣：")
print(X)
print("\n目標 (y) 長這樣：")
print(y)

from sklearn.tree import DecisionTreeClassifier

print("\n--- 召喚決策樹模型並開始訓練 ---")

# 1. 建立一個決策樹模型的實例 (就像是新生入學)
# random_state=42 是為了確保每次跑出來的結果都一樣，方便我們除錯
model = DecisionTreeClassifier(random_state=42)

# 2. 讓模型開始學習！(Fit 函數)
# 把特徵 (X) 和解答 (y) 給它，讓它自己找規律
model.fit(X, y)

print("模型訓練完成！🎓")



print("\n--- 🔮 AI 隨堂測驗：預測新遊戲 ---")

# 1. 虛構兩款新遊戲的資料
# 注意：餵給 AI 的特徵順序，必須跟訓練時一模一樣 (先 Price，再 TotalReviews)
# 遊戲 A (獨立小遊戲)：定價 4.99，剛上市只有 500 則評論
# 遊戲 B (3A 級大作)：定價 69.99，累積了 80 萬則評論
new_games = pd.DataFrame({
    'Price': [4.99, 69.99],
    'TotalReviews': [500, 800000]
})

print("我們請 AI 評估以下兩款新遊戲：")
print(new_games)

# 2. 呼叫 predict() 函數讓 AI 鐵口直斷！
predictions = model.predict(new_games)

# 3. 把 AI 的預測結果貼回表格中印出來
new_games['Predicted_Is_Hit'] = predictions

print("\n--- 📝 AI 預測結果出爐 ---")
print(new_games)









