from fastapi import APIRouter, HTTPException
from passlib.hash import bcrypt
from app.database import get_conn

router = APIRouter()

@router.post("/login")
def login(email: str, senha: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, senha_hash FROM usuarios WHERE email=%s AND ativo=true", (email,))
    u = cur.fetchone()
    if not u or not bcrypt.verify(senha, u[1]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"status": "ok"}
