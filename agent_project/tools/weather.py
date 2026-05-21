from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """获取指定城市的当前天气信息。当用户询问某个城市的天气时使用此工具。"""
    # 示例数据，实际项目中替换为真实 API 调用
    mock_data = {
        "北京": "晴，气温 28°C，湿度 45%",
        "上海": "多云，气温 25°C，湿度 70%",
        "广州": "小雨，气温 30°C，湿度 85%",
        "深圳": "阴天，气温 29°C，湿度 75%",
    }
    return mock_data.get(city, f"{city}：晴，气温 22°C，湿度 50%（模拟数据）")
