"""
简化的用户业务逻辑服务 - 使用内存存储
"""
from typing import List, Optional
from fastapi import HTTPException, status

from app.storage.memory import user_storage


class SimpleUserService:
    """简化的用户业务逻辑服务类"""
    
    def __init__(self):
        self.storage = user_storage
    
    def get_user(self, user_id: int) -> dict:
        """获取用户信息"""
        user = self.storage.get_user(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="用户不存在"
            )
        return user
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[dict]:
        """获取用户列表"""
        return self.storage.get_all_users(skip=skip, limit=limit)
    
    def create_user(self, user_data: dict) -> dict:
        """创建新用户"""
        # 检查用户名是否已存在
        if self.storage.get_user_by_username(user_data["username"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="用户名已存在"
            )
        
        # 检查邮箱是否已存在
        if self.storage.get_user_by_email(user_data["email"]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="邮箱已被注册"
            )
        
        return self.storage.create_user(user_data)
    
    def update_user(self, user_id: int, update_data: dict) -> Optional[dict]:
        """更新用户信息"""
        user = self.storage.get_user(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="用户不存在"
            )
        
        # 如果更新用户名，检查是否重复
        if "username" in update_data and update_data["username"] != user["username"]:
            if self.storage.get_user_by_username(update_data["username"]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="用户名已存在"
                )
        
        # 如果更新邮箱，检查是否重复
        if "email" in update_data and update_data["email"] != user["email"]:
            if self.storage.get_user_by_email(update_data["email"]):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="邮箱已被注册"
                )
        
        return self.storage.update_user(user_id, update_data)
    
    def delete_user(self, user_id: int) -> dict:
        """删除用户"""
        user = self.storage.delete_user(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="用户不存在"
            )
        return user


# 创建服务实例
simple_user_service = SimpleUserService() 