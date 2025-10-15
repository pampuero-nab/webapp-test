from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import home, about, contact

app = FastAPI()

# Static (CSS/JS/imagenes)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Routers (páginas)
app.include_router(home.router)
app.include_router(about.router)
app.include_router(contact.router)
