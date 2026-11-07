
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
import models

from routers.tasks import router as task_router
from routers.INTERVIEWS import router as interview_router


# Application details
app = FastAPI(
    title="Virtual HR",
    description="Virtual HR - Recruitment, Task Management and Interview Scheduling API",
    version="2.0.0"
)

from routers.candidates import router as candidate_router
app.include_router(candidate_router)
# CORS configuration
# Local development frontend
allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

# Add deployed frontend URL through environment variable
frontend_url = os.getenv("FRONTEND_URL")

if frontend_url:
    allowed_origins.append(frontend_url)


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables
Base.metadata.create_all(bind=engine)


# Register API routers
app.include_router(task_router)
app.include_router(interview_router)


# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to Virtual HR",
        "application": "Virtual HR Management System",
        "version": "2.0.0",
        "features": [
            "Task Management",
            "Task Progress Tracking",
            "Interview Scheduling",
            "Recruitment Management"
        ]
    }


# Health check API
@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(
                __import__("sqlalchemy").text("SELECT 1")
            )

        return {
            "status": "Application is running",
            "database": "Connected"
        }

    except Exception as error:
        return {
            "status": "Application is running",
            "database": "Disconnected",
            "error": str(error)
        }


# API information
@app.get("/api-info")
def api_info():
    return {
        "application": "Virtual HR",
        "version": "2.0.0",
        "documentation": "/docs",
        "health_check": "/health"
    }
