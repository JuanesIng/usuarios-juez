from fastapi import FastAPI
from app import models, database
from app.routes import ususarios
from app.auth_routes import router as auth_router

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
app.include_router(ususarios.router)
app.include_router(auth_router)