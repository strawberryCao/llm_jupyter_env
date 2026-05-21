from agent_project.tools.weather import get_weather
from agent_project.tools.calculator import calculate
from agent_project.tools.datetime_tool import get_current_time

# 所有可用工具列表 — 添加新工具时只需在这里加一行导入
ALL_TOOLS = [get_weather, calculate, get_current_time]
