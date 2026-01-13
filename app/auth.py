from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import os
from app.database import get_conn

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

JWT_SECRET = os.getenv("JWT_SECRET", "fallback_secret")
ALGORITHM = "HS256"

def criar_token(user_id: str, perfil: str):
    payload = {
        "sub": user_id,
        "perfil": perfil,
        "exp": datetime.utcnow() + timedelta(hours=8)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)

@router.post("/login")
def login(email: str, senha: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, senha_hash, perfil, primeiro_login FROM usuarios WHERE email=%s AND ativo=true",
            (email,)
        )
        u = cur.fetchone()

        if not u:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")

        if not pwd_context.verify(senha, u[1]):
            raise HTTPException(status_code=401, detail="Senha inválida")

        token = criar_token(str(u[0]), u[2])

        return {
            "access_token": token,
            "perfil": u[2],
            "primeiro_login": u[3]
        }

    except HTTPException:
        raise
    except Exception as e:
        import traceback
        print("ERRO LOGIN:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Erro interno no login")
