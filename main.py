from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title="NotebookUm API Gateway",
    description="Microservicio controlador de llamadas para NotebookUm.",
    version="0.1.0",
)

@app.get("/healthz")
def health_check():
    return {"status": "ok", "service": "notebookum-controller"}
