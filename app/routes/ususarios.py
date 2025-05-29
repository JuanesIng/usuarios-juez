from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.UserOut)
def crear_usuario(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, user)

@router.get("/", response_model=list[schemas.UserOut])
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_usuarios(db, skip, limit)

@router.get("/{user_id}", response_model=schemas.UserOut)
def listar_usuario(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_usuario(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@router.put("/{user_id}", response_model=schemas.UserOut)
def actualizar_usuario(user_id: int, user: schemas.ActualizarUsuario, db: Session = Depends(get_db)):
    db_user = crud.actualizar_usuario(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user

@router.delete("/{user_id}")
def eliminar_usuario(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.eliminar_usuario(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"ok": True}
