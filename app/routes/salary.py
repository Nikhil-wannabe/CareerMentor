from fastapi import APIRouter
from services.jsearch import fetch_jobs

router = APIRouter()

@router.get("/")
def get_salary(role: str, location: str = "United States"):
    jobs = fetch_jobs(role, location)
    salaries = []
    for job in jobs:
        # JSearch may provide salary in a field like "job_salary"
        salary = job.get("job_salary", None)
        if salary:
            salaries.append(salary)
    
    return {"role": role, "salary_data": salaries}
