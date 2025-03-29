import requests
import os

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

def fetch_jobs(role: str, location: str = "United States", page: int = 1):
    url = "https://jsearch.p.rapidapi.com/search"
    querystring = {
        "query": role,
        "location": location,
        "page": str(page),
        "num_pages": "1"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    return data.get("data", [])
