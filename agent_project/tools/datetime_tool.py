from datetime import datetime
from langchain_core.tools import tool


@tool
def get_current_time() -> str:
    """获取当前的日期和时间。当用户询问现在几点或今天日期时使用此工具。"""
    now = datetime.now()
    return now.strftime("%Y年%m月%d日 %H:%M:%S（星期%w）").replace(
        "星期0", "星期日"
    ).replace(
        "星期1", "星期一"
    ).replace(
        "星期2", "星期二"
    ).replace(
        "星期3", "星期三"
    ).replace(
        "星期4", "星期四"
    ).replace(
        "星期5", "星期五"
    ).replace(
        "星期6", "星期六"
    )
