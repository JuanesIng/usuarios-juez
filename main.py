from fastapi import FastAPI
from app import models, database
from app.routes import ususarios

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)
app.include_router(ususarios.router)