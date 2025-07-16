"""
页面路由端点
"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.config import settings

router = APIRouter()
templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """首页"""
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "title": "欢迎访问我的网站"}
    )


@router.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    """关于页面"""
    return templates.TemplateResponse(
        "about.html", 
        {"request": request, "title": "关于我们"}
    ) 