"""
API v1路由聚合
"""
from fastapi import APIRouter

from app.api.v1.endpoints import pages, basic, users_simple

api_router = APIRouter()

# 包含各个模块的路由
api_router.include_router(basic.router, prefix="/basic", tags=["基础API"])
api_router.include_router(users_simple.router, prefix="/users", tags=["用户管理"])
api_router.include_router(pages.router, tags=["页面"]) 