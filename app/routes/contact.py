from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")
router = APIRouter(tags=["contact"], prefix="/contact")

@router.get("", name="contact:contact_get")
def contact_get(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@router.post("", name="contact:contact_post")
def contact_post(
    request: Request,
    nombre: str = Form(...),
    email: str = Form(...),
    mensaje: str = Form(...)
):
    # aquí podría enviar email/guardar en DB
    ctx = {"request": request, "enviado": True, "nombre": nombre}
    return templates.TemplateResponse("contact.html", ctx)
