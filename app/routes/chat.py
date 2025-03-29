from fastapi import APIRouter, HTTPException
import re
import requests
import os

router = APIRouter()

# Define endpoints for internal API calls (assuming they're hosted on the same server)
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def detect_intent(query: str):
    query = query.lower()
    if "salary" in query:
        return "salary"
    elif "trend" in query or "hiring" in query or "where" in query:
        # "where" can hint at market trends
        return "trends"
    elif "resume" in query or "upload" in query:
        return "resume"
    else:
        # Default to trends for now
        return "trends"

def extract_role(query: str):
    # This is a simplistic extraction: look for common role keywords
    roles = ["data scientist", "ml engineer", "data analyst", "software engineer"]
    for role in roles:
        if role in query:
            return role
    return "Data Scientist"  # default role

@router.post("/")
def chat(query: str):
    intent = detect_intent(query)
    role = extract_role(query)
    location = "United States"  # Could be enhanced with more parsing

    # Route the query to the appropriate API endpoint
    if intent == "salary":
        url = f"{BASE_URL}/salary/?role={role}&location={location}"
    elif intent == "trends":
        url = f"{BASE_URL}/trends/?role={role}&location={location}"
    elif intent == "resume":
        return {"message": "Please upload your resume through the resume analyzer endpoint."}
    else:
        raise HTTPException(status_code=400, detail="Intent not recognized")

    # Make a GET request to the chosen endpoint
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching data")
    data = response.json()

    # Return a conversational response
    return {
        "query": query,
        "detected_intent": intent,
        "role": role,
        "response": data
    }
