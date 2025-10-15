from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Hola FastAPI"})

@app.post("/saludo", response_class=HTMLResponse)
def saludo(request: Request, nombre: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "title": f"Hola {nombre}!"})
