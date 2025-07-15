from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

# 创建FastAPI应用实例
app = FastAPI(
    title="My Web Site",
    description="一个基于FastAPI的现代web站点",
    version="1.0.0"
)

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板引擎
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """首页路由"""
    return templates.TemplateResponse("index.html", {"request": request, "title": "欢迎访问我的网站"})

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    """关于页面路由"""
    return templates.TemplateResponse("about.html", {"request": request, "title": "关于我们"})

@app.get("/api/hello")
async def hello_api():
    """API接口示例"""
    return {"message": "Hello, World!", "status": "success"}

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    """用户API示例"""
    return {"user_id": user_id, "name": f"用户{user_id}", "status": "active"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 