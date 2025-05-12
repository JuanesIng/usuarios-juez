# app/auth.py
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from jose import JWTError
from app.auth import crear_acceso_token
from pydantic import BaseModel

# Pydantic para la solicitud de login
class LoginData(BaseModel):
    email: str
    contrasenna: str

# Función que valida usuario
def autenticar_usuario(db: Session, email: str, contrasenna: str):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if not usuario or usuario.contrasenna != contrasenna:
        return None
    return usuario

# Endpoint de login
from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(datos: LoginData, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, datos.email, datos.contrasenna)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas"
        )
    
    # Crear el token con el id del usuario
    access_token = crear_acceso_token(
        data={"sub": usuario.email}  # puedes guardar el email o el id
    )
    return {"access_token": access_token, "token_type": "bearer"}
