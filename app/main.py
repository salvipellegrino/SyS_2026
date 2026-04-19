from app.routers import health
from fastapi import FastAPI

app = FastAPI()

app.include_router(health.router)


@app.get("/")
def root():
    return {"message": "RIR API funcionando"}
