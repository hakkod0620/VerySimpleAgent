import os

from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(find_dotenv())


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("找不到 GOOGLE_API_KEY！檢查 .env 檔案名稱與位置。")
else:
    print("讀取到 API Key！")


print("--- 啟動 Gemini  ---")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt = "你現在是一位頂級的 Steam 遊戲市場分析師。請用 50 個字以內，向我打個招呼。"

print(f"我們對 AI 說：{prompt}\n")
print("AI 思考中...\n")


response = llm.invoke(prompt)

print("--- 首次報到 ---")
print(response.content)
