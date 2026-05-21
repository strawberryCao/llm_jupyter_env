import os
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

MODEL_NAME = "deepseek-chat"
TEMPERATURE = 0.0

SYSTEM_PROMPT = "你是一个有用的AI助手，可以使用工具来帮助用户解决问题。请用中文回答。"
