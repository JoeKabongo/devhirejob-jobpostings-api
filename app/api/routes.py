from fastapi import APIRouter 

router = APIRouter(prefix="/api/v1/jobs")

@router.get("/") 
def posted_jobs():
    return []