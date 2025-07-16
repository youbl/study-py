"""
FastAPI主应用入口
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
# from app.core.database import create_tables
from app.api.v1.api import api_router


def create_app() -> FastAPI:
    """创建FastAPI应用实例"""
    
    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        debug=settings.DEBUG
    )
    
    # 添加CORS中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # 挂载静态文件
    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
    
    # 包含API路由
    app.include_router(api_router, prefix="/api/v1")
    
    # 创建数据库表
    # create_tables()
    
    return app


# 创建应用实例
app = create_app() 