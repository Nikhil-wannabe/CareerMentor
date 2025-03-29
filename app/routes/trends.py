from fastapi import APIRouter
from collections import defaultdict
from services.jsearch import fetch_jobs

router = APIRouter()

@router.get("/")
def get_trends(role: str, location: str = "United States"):
    # For simplicity, get first page of jobs
    jobs = fetch_jobs(role, location)
    
    # Aggregate count per employer to show which companies are hiring
    company_counts = defaultdict(int)
    for job in jobs:
        company = job.get("employer_name", "Unknown")
        company_counts[company] += 1
    
    return {"role": role, "trend_data": dict(company_counts)}
