from fastapi import FastAPI
from app.auth import router as auth_router
from app.fotos import router as fotos_router

app = FastAPI(title="Sanesul Backend")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(fotos_router, prefix="/fotos", tags=["Fotos"])
