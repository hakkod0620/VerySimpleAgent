import os
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent


load_dotenv(find_dotenv())

print("--- 讀取 Steam 遊戲資料庫 ---")
df = pd.read_csv("steam_games.csv")


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


print("--- Agent ---")
agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True, 
    allow_dangerous_code=True,
    handle_parsing_errors=True 
)

print("\n準備就緒！")


question = "看一下這份資料，哪一款遊戲的好評數最高？叫什麼名字？"
print(f"：{question}\n")


response = agent.invoke(question)

print("\n--- 最終報告 ---")
print(response["output"])
