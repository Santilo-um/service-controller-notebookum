import httpx
from fastapi import APIRouter, HTTPException
from app.config import settings

router = APIRouter()


@router.get("/orchestrate")
async def orchestrate():
    """
    Call the upstream NotebookUm service and return its response.
    Handles timeouts and service errors with appropriate HTTP status codes.
    """
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                f"{settings.NOTEBOOKUM_SERVICE_URL}/orchestrate"
            )
            
            # If upstream returns an error, propagate it as 502 Bad Gateway
            if response.status_code >= 400:
                raise HTTPException(
                    status_code=502,
                    detail=f"Upstream service returned {response.status_code}"
                )
            
            return response.json()
    
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=503,
            detail="Upstream service timeout - check connectivity"
        )
    
    except httpx.ConnectError:
        raise HTTPException(
            status_code=502,
            detail="Cannot reach upstream service - service may be down"
        )
    
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=502,
            detail=f"Request to upstream failed: {str(e)}"
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Unexpected error: {str(e)}"
        )
