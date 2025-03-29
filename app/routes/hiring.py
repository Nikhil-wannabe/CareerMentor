from fastapi import APIRouter
from collections import defaultdict
from services.jsearch import fetch_jobs

router = APIRouter()

@router.get("/")
def get_hiring(role: str, location: str = "United States"):
    jobs = fetch_jobs(role, location)
    
    # Count jobs by posting date if available.
    # JSearch might have a field like "job_posted_at_datetime_utc".
    # For this example, we'll just return the count.
    job_count = len(jobs)
    
    return {"role": role, "hiring_data": {"job_count": job_count}}
