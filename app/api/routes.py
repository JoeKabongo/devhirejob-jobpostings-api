from fastapi import APIRouter 
from app.services.japan_dev_scraper import get_posted_jobs

router = APIRouter(prefix="/api/v1/jobs")

@router.get("/japan-dev") 
def posted_jobs():
    """
    Endpoint to retrieve the latest job listings from Japan Dev.
    """
    return get_posted_jobs()
