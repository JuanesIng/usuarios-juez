from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

class UsuarioRol(str, enum.Enum):
    usuario = "usuario"
    admin = "admin"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombreUsu = Column(String, unique=True, index=True, nullable=False)
    apellidoUsu = Column(String, unique=True, index=True, nullable=False)
    contrasenna = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    rol = Column(Enum(UsuarioRol), default=UsuarioRol.usuario)
