from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(tags=["home"], prefix="")
# nombre del router para url_for: "home"
router.default_response_class = HTMLResponse

@router.get("/", name="home:home")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
