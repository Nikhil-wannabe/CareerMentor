from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import trends, salary, hiring, resume, chat
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trends.router, prefix="/trends")
app.include_router(salary.router, prefix="/salary")
app.include_router(hiring.router, prefix="/hiring")
app.include_router(resume.router, prefix="/resume")
app.include_router(chat.router, prefix="/chat")

@app.get("/")
def root():
    return {"message": "CareerMentor API is running"}
