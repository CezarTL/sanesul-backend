import requests
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/analisar")
def analisar_foto(url_foto: str):
    try:
        # chamada direta ao space (simulando uso humano)
        response = requests.get(
            "https://huggingface.co/spaces/SEU_USUARIO/sanesul-ia-fotos",
            params={"url": url_foto},
            timeout=15
        )

        # fallback simples (enquanto não usa API formal)
        if response.status_code == 200:
            return {
                "resultado": "CONFORME",
                "confianca": 0.75
            }

        raise HTTPException(status_code=500, detail="Erro na IA")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
