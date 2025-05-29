from sqlalchemy.orm import Session
from app import models, schemas

def get_usuario(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def crear_usuario(db: Session, user: schemas.UserCreate):
    db_usuario = models.Usuario(**user.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def actualizar_usuario(db: Session, user_id: int, user: schemas.ActualizarUsuario):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if db_usuario:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, user_id: int):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == user_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario
