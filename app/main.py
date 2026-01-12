from fastapi import FastAPI
from app import auth, usuarios, rtm, fotos, ie, dashboard, feriados

app = FastAPI(title="Sanesul IA")

app.include_router(auth.router, prefix="/auth")
app.include_router(usuarios.router, prefix="/usuarios")
app.include_router(rtm.router, prefix="/rtm")
app.include_router(fotos.router, prefix="/fotos")
app.include_router(ie.router, prefix="/ie")
app.include_router(dashboard.router, prefix="/dashboard")
app.include_router(feriados.router, prefix="/feriados")
