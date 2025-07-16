"""
简化的用户API端点 - 使用内存存储
"""
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.services.user_service_simple import simple_user_service

router = APIRouter()


class UserCreate(BaseModel):
    """创建用户的输入模型"""
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool = True


class UserUpdate(BaseModel):
    """更新用户的输入模型"""
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


@router.get("/", response_model=List[Dict[str, Any]])
def get_users(skip: int = 0, limit: int = 100):
    """获取用户列表"""
    return simple_user_service.get_users(skip=skip, limit=limit)


@router.get("/{user_id}", response_model=Dict[str, Any])
def get_user(user_id: int):
    """根据ID获取用户信息"""
    return simple_user_service.get_user(user_id=user_id)


@router.post("/", response_model=Dict[str, Any], status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate):
    """创建新用户"""
    user_data = user_create.dict()
    return simple_user_service.create_user(user_data)


@router.put("/{user_id}", response_model=Dict[str, Any])
def update_user(user_id: int, user_update: UserUpdate):
    """更新用户信息"""
    update_data = user_update.dict(exclude_unset=True)
    return simple_user_service.update_user(user_id=user_id, update_data=update_data)


@router.delete("/{user_id}", response_model=Dict[str, Any])
def delete_user(user_id: int):
    """删除用户"""
    return simple_user_service.delete_user(user_id=user_id) 