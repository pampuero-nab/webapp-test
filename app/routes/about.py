from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(tags=["about"], prefix="/about")

@router.get("", name="about:about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
