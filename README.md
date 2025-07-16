# FastAPI Web 站点项目 (MVC架构)

一个基于 FastAPI 构建的现代化 web 站点项目，采用标准的 MVC 分层架构设计，展示了企业级 web 应用开发的最佳实践。

## 功能特性

- ✅ **MVC分层架构**: 清晰的模型-视图-控制器分离
- ✅ **现代化框架**: 基于 FastAPI 的高性能 web 框架
- ✅ **数据库集成**: SQLAlchemy ORM + SQLite 数据库
- ✅ **业务逻辑分离**: 独立的服务层处理业务逻辑
- ✅ **RESTful API**: 标准的 REST API 设计
- ✅ **响应式设计**: 使用 Bootstrap 5 构建的现代化 UI
- ✅ **模板系统**: Jinja2 模板引擎支持
- ✅ **自动文档**: 自动生成的 API 文档 (Swagger UI)
- ✅ **依赖注入**: FastAPI 的依赖注入系统
- ✅ **配置管理**: 集中化的配置管理
- ✅ **开发友好**: 热重载和详细错误信息

## 技术栈

- **后端框架**: FastAPI + Uvicorn
- **数据库**: SQLAlchemy + SQLite
- **模式验证**: Pydantic
- **模板引擎**: Jinja2
- **前端**: Bootstrap 5 + 原生 JavaScript
- **Python 版本**: 3.7+

## 项目结构 (MVC架构)

```
py-mcp/
├── app/                    # 主应用包
│   ├── __init__.py
│   ├── main.py            # FastAPI应用入口
│   ├── api/               # API层 (Controller)
│   │   ├── __init__.py
│   │   └── v1/            # API版本v1
│   │       ├── __init__.py
│   │       ├── api.py     # 路由聚合
│   │       └── endpoints/ # API端点
│   │           ├── __init__.py
│   │           ├── basic.py    # 基础API
│   │           ├── users.py    # 用户API
│   │           └── pages.py    # 页面路由
│   ├── core/              # 核心配置
│   │   ├── __init__.py
│   │   ├── config.py      # 应用配置
│   │   └── database.py    # 数据库配置
│   ├── models/            # 数据模型层 (Model)
│   │   ├── __init__.py
│   │   └── user.py        # 用户模型
│   ├── schemas/           # Pydantic模式
│   │   ├── __init__.py
│   │   └── user.py        # 用户模式
│   ├── crud/              # 数据访问层
│   │   ├── __init__.py
│   │   └── user.py        # 用户CRUD操作
│   ├── services/          # 业务逻辑层
│   │   ├── __init__.py
│   │   └── user_service.py # 用户业务逻辑
│   └── utils/             # 工具函数
│       ├── __init__.py
│       └── common.py      # 通用工具
├── templates/             # HTML模板 (View)
│   ├── base.html          # 基础模板
│   ├── index.html         # 首页
│   └── about.html         # 关于页面
├── static/               # 静态文件
│   ├── css/
│   │   └── style.css     # 自定义样式
│   └── js/
│       └── main.js       # JavaScript 功能
├── run.py                # 应用启动文件
├── requirements.txt      # 项目依赖
├── README.md            # 项目说明
└── .gitignore           # Git忽略文件
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
python run.py
```

或者使用 uvicorn 直接运行：

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. 访问应用

- **主页**: http://localhost:8000/
- **关于页面**: http://localhost:8000/about
- **API 文档**: http://localhost:8000/docs
- **ReDoc 文档**: http://localhost:8000/redoc

## API 接口

### 页面路由

- `GET /` - 首页
- `GET /about` - 关于页面

### 基础API (v1)

- `GET /api/v1/basic/hello` - Hello World API
- `GET /api/v1/basic/health` - 健康检查
- `GET /api/v1/basic/version` - 版本信息

### 用户管理API (v1)

- `GET /api/v1/users/` - 获取用户列表
- `GET /api/v1/users/{user_id}` - 获取用户信息
- `POST /api/v1/users/` - 创建用户
- `PUT /api/v1/users/{user_id}` - 更新用户
- `DELETE /api/v1/users/{user_id}` - 删除用户

### 示例请求

```bash
# 测试 Hello API
curl http://localhost:8000/api/v1/basic/hello

# 健康检查
curl http://localhost:8000/api/v1/basic/health

# 获取用户列表
curl http://localhost:8000/api/v1/users/

# 创建用户
curl -X POST "http://localhost:8000/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "full_name": "Test User"}'
```

## 开发指南

### 添加新页面

1. 在 `templates/` 目录创建新的 HTML 模板
2. 在 `main.py` 中添加对应的路由
3. 如需要，在 `static/` 目录添加相关的 CSS 和 JS 文件

### 添加新 API

在 `main.py` 中添加新的路由函数：

```python
@app.get("/api/your-endpoint")
async def your_api_function():
    return {"message": "Your response"}
```

### 自定义样式

编辑 `static/css/style.css` 文件来自定义网站样式。

## 部署

### 生产环境部署

```bash
# 使用 gunicorn (推荐)
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

# 或者使用 uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Docker 部署

创建 `Dockerfile`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！ 