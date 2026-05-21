from langchain_core.tools import tool


@tool
def calculate(expression: str) -> str:
    """计算数学表达式并返回结果。支持加减乘除、幂运算等。例如: '2 + 3 * 4' 或 '2 ** 10'。"""
    allowed_chars = set("0123456789+-*/.() ")
    if not all(c in allowed_chars for c in expression):
        return f"错误：表达式包含不允许的字符，仅支持数字和运算符"
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"计算错误：{e}"
