# FastAPI Web 站点项目

一个基于 FastAPI 构建的现代化 web 站点项目，展示了完整的 web 应用开发流程。

## 功能特性

- ✅ **现代化框架**: 基于 FastAPI 的高性能 web 框架
- ✅ **响应式设计**: 使用 Bootstrap 5 构建的现代化 UI
- ✅ **模板系统**: Jinja2 模板引擎支持
- ✅ **静态文件服务**: CSS、JavaScript 和图片资源管理
- ✅ **API 接口**: RESTful API 设计
- ✅ **自动文档**: 自动生成的 API 文档 (Swagger UI)
- ✅ **开发友好**: 热重载和详细错误信息

## 技术栈

- **后端**: FastAPI + Uvicorn
- **模板引擎**: Jinja2
- **前端**: Bootstrap 5 + 原生 JavaScript
- **Python 版本**: 3.7+

## 项目结构

```
py-mcp/
├── main.py                 # 主应用文件
├── requirements.txt        # 项目依赖
├── README.md              # 项目说明
├── templates/             # HTML 模板
│   ├── base.html          # 基础模板
│   ├── index.html         # 首页
│   └── about.html         # 关于页面
└── static/               # 静态文件
    ├── css/
    │   └── style.css     # 自定义样式
    └── js/
        └── main.js       # JavaScript 功能
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行应用

```bash
python main.py
```

或者使用 uvicorn 直接运行：

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. 访问应用

- **主页**: http://localhost:8000
- **关于页面**: http://localhost:8000/about
- **API 文档**: http://localhost:8000/docs
- **ReDoc 文档**: http://localhost:8000/redoc

## API 接口

### 基础接口

- `GET /` - 首页
- `GET /about` - 关于页面
- `GET /api/hello` - Hello World API
- `GET /api/users/{user_id}` - 获取用户信息

### 示例请求

```bash
# 测试 Hello API
curl http://localhost:8000/api/hello

# 获取用户信息
curl http://localhost:8000/api/users/123
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