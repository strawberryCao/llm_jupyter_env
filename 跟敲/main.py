from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("mcp")


@mcp.tool()
def calculate(expression: str) -> str:
    """
    计算简单数学表达式。

    支持：
    - sin(x)
    - cos(x)
    - sqrt(x)

    示例：
    calculate("sqrt(9)")
    calculate("sin(1)")
    """
    import math

    allowed = {
        "sin": math.sin,
        "cos": math.cos,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
    }

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
            allowed,
        )
        return f"{expression} = {result}"
    except Exception as e:
        return f"计算错误：{e}"


@mcp.tool()
def get_location() -> str:
    """
    获取当前默认位置。
    """
    return "汕头"


@mcp.tool()
def get_weather(city: str) -> str:
    """
    根据城市名获取天气信息。

    参数：
    city: 城市中文名，例如：汕头、广州、深圳、北京
    """
    import requests
    import time

    try:
        t = int(time.time() * 1000)

        response = requests.get(
            f"https://weather.cma.cn/api/map/weather/1?t={t}",
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://weather.cma.cn/",
            },
        )

        response.raise_for_status()
        json_data = response.json()

        city_list = json_data.get("data", {}).get("city", [])

        if not city_list:
            return f"获取天气失败：接口返回中没有 city 数据，原始字段为：{list(json_data.keys())}"

        matched = []

        for item in city_list:
            text = str(item)

            if city in text or city.replace("市", "") in text:
                matched.append(item)

        if matched:
            return f"{city} 的天气数据：{matched[:3]}"

        sample = city_list[:5]
        return f"没有找到城市：{city}。接口返回城市样例：{sample}"

    except Exception as e:
        return f"获取天气失败：{repr(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")