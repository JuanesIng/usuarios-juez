from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app import auth, crud, database

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login", summary="Custom login returning JWT token")
def custom_login(login_data: LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, login_data.email)
    if not user or not auth.verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_token({"sub": user.email, "rol": user.role})
    return {"access_token": token, "token_type": "bearer"}
