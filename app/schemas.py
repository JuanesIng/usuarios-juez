from pydantic import BaseModel
from typing import Optional
from enum import Enum

class UsuarioRol(str, Enum):
    usuario = "usuario"
    admin = "admin"

class UsuarioBase(BaseModel):
    nombreUsu: str
    apellidoUsu: str
    contrasenna: str
    email: str
    rol: UsuarioRol = UsuarioRol.usuario

class UserCreate(UsuarioBase):
    pass

class ActualizarUsuario(BaseModel):
    nombreUsu: Optional[str]
    apellidoUsu: Optional[str]
    contrasenna: Optional[str]
    rol: Optional[UsuarioRol]

class UserOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
