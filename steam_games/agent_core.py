import os
# 多匯入一個 find_dotenv 尋寶工具
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())

# 1. 載入隱藏的密碼檔 (.env)
load_dotenv()

# --- 新增的除錯檢查哨 ---
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ 警告：找不到 GOOGLE_API_KEY！請檢查 .env 檔案名稱與位置。")
else:
    print("✅ 成功讀取到 API Key！準備連線...")
# ----------------------

print("--- 啟動 Gemini 人工智慧大腦 ---")

# 2. 初始化 Gemini 模型 
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 3. 給 AI 下達第一個任務指令 (Prompt)
prompt = "你現在是一位頂級的 Steam 遊戲市場分析師。請用 50 個字以內，向我（你的老闆）簡單打個招呼，並展現一下你的專業態度。"

print(f"我們對 AI 說：{prompt}\n")
print("AI 思考中...\n")

# 4. 執行呼叫 (Invoke)
response = llm.invoke(prompt)

print("--- 🤖 AI 分析師的首次報到 ---")
print(response.content)