from fastapi import APIRouter

router = APIRouter()

@router.get("/orchestrate")
def orchestrate():
    return {"status": "pending"}
