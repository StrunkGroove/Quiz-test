from fastapi import FastAPI
from app.api.endpoints.v1 import quiz

app = FastAPI()

app.include_router(quiz.router)