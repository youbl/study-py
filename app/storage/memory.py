"""
内存数据存储层 - 替代数据库进行演示
"""
from typing import Dict, List, Optional
from datetime import datetime


class InMemoryUserStorage:
    """内存用户数据存储"""
    
    def __init__(self):
        self._users: Dict[int, dict] = {}
        self._next_id = 1
        
        # 预置一些示例数据
        self._add_sample_data()
    
    def _add_sample_data(self):
        """添加示例数据"""
        sample_users = [
            {"username": "admin", "email": "admin@example.com", "full_name": "管理员"},
            {"username": "user1", "email": "user1@example.com", "full_name": "用户1"},
            {"username": "user2", "email": "user2@example.com", "full_name": "用户2"},
        ]
        
        for user_data in sample_users:
            self.create_user(user_data)
    
    def get_user(self, user_id: int) -> Optional[dict]:
        """根据ID获取用户"""
        return self._users.get(user_id)
    
    def get_user_by_username(self, username: str) -> Optional[dict]:
        """根据用户名获取用户"""
        for user in self._users.values():
            if user["username"] == username:
                return user
        return None
    
    def get_user_by_email(self, email: str) -> Optional[dict]:
        """根据邮箱获取用户"""
        for user in self._users.values():
            if user["email"] == email:
                return user
        return None
    
    def get_all_users(self, skip: int = 0, limit: int = 100) -> List[dict]:
        """获取所有用户"""
        users = list(self._users.values())
        return users[skip:skip + limit]
    
    def create_user(self, user_data: dict) -> dict:
        """创建用户"""
        user = {
            "id": self._next_id,
            "username": user_data["username"],
            "email": user_data["email"],
            "full_name": user_data.get("full_name"),
            "is_active": user_data.get("is_active", True),
            "created_at": datetime.now(),
            "updated_at": None
        }
        
        self._users[self._next_id] = user
        self._next_id += 1
        return user
    
    def update_user(self, user_id: int, update_data: dict) -> Optional[dict]:
        """更新用户"""
        if user_id not in self._users:
            return None
        
        user = self._users[user_id]
        for key, value in update_data.items():
            if key != "id" and value is not None:
                user[key] = value
        
        user["updated_at"] = datetime.now()
        return user
    
    def delete_user(self, user_id: int) -> Optional[dict]:
        """删除用户"""
        return self._users.pop(user_id, None)


# 创建全局存储实例
user_storage = InMemoryUserStorage() 