import asyncio
import sys
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent


# 读取项目根目录 .env
ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)


async def main():
    mcp_client = MultiServerMCPClient(
        {
            "my_mcp": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [
                    r"C:\Users\ASUS\Desktop\llm_jupyter_env\跟敲\main.py",
                ],
            },
            "tavily": {
                "transport": "stdio",
                "command": "npx.cmd",
                "args": [
                    "-y",
                    "tavily-mcp",
                ],
                "env": {
                    "TAVILY_API_KEY": os.getenv("TAVILY_API_KEY", ""),
                },
            },
        }
    )

    mcp_tools = await mcp_client.get_tools()

    for tool in mcp_tools:
        print(tool.name)

    llm = ChatDeepSeek(
        model="deepseek-v4-flash",
        temperature=0,
    )

    agent = create_agent(
        model=llm,
        tools=mcp_tools,
    )

    response = await agent.ainvoke(
        {
            "messages": [
                SystemMessage(
                    (
                        "你是一个会主动调用工具的助手。"
                        "需要默认位置或本地天气时，优先调用 my_mcp 工具；"
                        "需要联网搜索、最新信息、网页信息时，优先调用 tavily 工具。"
                    )
                ),
                HumanMessage(
                    "请先调用工具获取当前默认位置和汕头天气，再联网搜索今天有关人工智能的一个最新新闻，并总结。"
                    "今天的日期是什么？"
                ),
            ]
        }
    )

    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())