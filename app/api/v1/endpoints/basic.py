"""
基本API端点
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def hello_world():
    """Hello World API"""
    return {"message": "Hello, World!", "status": "success"}


@router.get("/health")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy", "message": "服务运行正常"}


@router.get("/version")
async def get_version():
    """获取API版本信息"""
    return {
        "version": "1.0.0",
        "api_version": "v1",
        "framework": "FastAPI"
    } 