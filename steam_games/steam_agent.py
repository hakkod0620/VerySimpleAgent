import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# 1. 讀取金鑰
load_dotenv(find_dotenv())

print("--- 讀取 Steam 遊戲資料庫 ---")
df = pd.read_csv("steam_games.csv")

# 2. 喚醒 Gemini 大腦
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 3. 融合大腦與雙手，啟動 AI Agent (加入救星 handle_parsing_errors=True)
print("--- 融合大腦與雙手，啟動 AI Agent ---")
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True, 
    allow_dangerous_code=True,
    handle_parsing_errors=True  # 🌟 讓 AI 遇到格式錯誤時能自我修復！
)

print("\n🤖 分析師準備就緒！")

# 4. 老闆 (你) 下達任務
question = "請幫我看一下這份資料，哪一款遊戲的好評數 (PositiveReviews) 最高？它叫什麼名字？"
print(f"老闆問：{question}\n")

# 5. 讓 Agent 自己去想辦法找答案
response = agent.invoke(question)

print("\n--- 📊 分析師的最終報告 ---")
print(response["output"])