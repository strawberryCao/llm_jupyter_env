from langchain_deepseek import ChatDeepSeek
from langgraph.prebuilt import create_react_agent

from agent_project.config.settings import MODEL_NAME, TEMPERATURE, SYSTEM_PROMPT, DEEPSEEK_API_KEY
from agent_project.tools import ALL_TOOLS


def create_agent():
    """创建并返回一个带工具的 agent。"""
    llm = ChatDeepSeek(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        api_key=DEEPSEEK_API_KEY,
    )
    agent = create_react_agent(llm, ALL_TOOLS, prompt=SYSTEM_PROMPT)
    return agent


def run_agent(query: str) -> str:
    """快捷方式：创建 agent 并执行一次查询，返回最终回复文本。"""
    agent = create_agent()
    result = agent.invoke({"messages": [("user", query)]})
    return result["messages"][-1].content
