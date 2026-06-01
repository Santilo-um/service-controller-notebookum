from fastapi import FastAPI
from app.config import settings
from app.controllers.orchestration import router as orchestration_router

app = FastAPI(
    title="NotebookUm API Gateway",
    description="Microservicio controlador de llamadas para NotebookUm.",
    version="0.1.0",
)

app.include_router(orchestration_router)

@app.get("/healthz")
def health_check():
    return {"status": "ok", "service": "notebookum-controller"}
