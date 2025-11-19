from fastapi import FastAPI
from controller import bank_controller
import queries 
from database import db
import logging

app = FastAPI(title="Bank API", version="1.0")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

@app.on_event("startup")
def startup_event():
    with db.get_cursor() as cursor:
        cursor.execute(queries.CREATE_BANK_TABLE)
    logger.info("Bank table initialized successfully")

app.include_router(bank_controller.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Bank API"}

