"""
应用配置设置
"""
from typing import List


class Settings:
    """应用设置"""
    
    # 应用基本信息
    APP_NAME: str = "FastAPI Web Site"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "一个基于FastAPI的现代web站点"
    
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./app.db"
    
    # 安全配置
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS配置
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # 静态文件配置
    STATIC_DIR: str = "static"
    TEMPLATES_DIR: str = "templates"


# 创建设置实例
settings = Settings() 