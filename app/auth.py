from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from datetime import datetime, timedelta
from jose import jwt
import os
from app.database import get_conn

router = APIRouter()

JWT_SECRET = os.getenv("JWT_SECRET")
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
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, senha_hash, perfil, primeiro_login FROM usuarios WHERE email=%s AND ativo=true",
        (email,)
    )
    u = cur.fetchone()

    if not u or not bcrypt.verify(senha, u[1]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token(str(u[0]), u[2])

    return {
        "access_token": token,
        "perfil": u[2],
        "primeiro_login": u[3]
    }
