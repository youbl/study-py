"""
通用工具函数
"""
from datetime import datetime
from typing import Any, Dict


def format_datetime(dt: datetime) -> str:
    """格式化日期时间"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def create_response(data: Any = None, message: str = "success", code: int = 200) -> Dict:
    """创建统一的API响应格式"""
    return {
        "code": code,
        "message": message,
        "data": data,
        "timestamp": format_datetime(datetime.now())
    } 