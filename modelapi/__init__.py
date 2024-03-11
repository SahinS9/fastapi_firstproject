from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from modelapi import database, crud, models, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

from modelapi import routes