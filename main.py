from fastapi import FastAPI, HTTPException
from app.config import settings

app = FastAPI(
    title="NotebookUm API Gateway",
    description="Microservicio controlador de llamadas para NotebookUm.",
    version="0.1.0",
)

@app.get("/healthz")
def health_check():
    return {"status": "ok", "service": "notebookum-controller"}

@app.get("/orchestrate")
def orchestrate():
    if not settings.NOTEBOOKUM_SERVICE_URL:
        raise HTTPException(status_code=500, detail="NotebookUm service URL no está configurado")

    return {
        "message": "Controlador de llamadas operativo",
        "notebookum_service_url": settings.NOTEBOOKUM_SERVICE_URL,
    }
