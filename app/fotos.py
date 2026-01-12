import os
import requests
from fastapi import APIRouter
from app.database import get_conn

router = APIRouter()
IA_API = os.getenv("IA_API_URL")

@router.post("/analisar")
def analisar_foto(url_foto: str):
    r = requests.post(
        f"{IA_API}/run/predict",
        json={"data": [url_foto]},
        timeout=20
    )

    resultado, confianca = r.json()["data"]

    return {
        "resultado": resultado,
        "confianca": confianca
    }
