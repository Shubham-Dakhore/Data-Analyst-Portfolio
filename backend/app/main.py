# File: backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
import os




from app.database.connection import (
    engine,
    Base
)

from app.database import models

from app.routes.auth import (
    router as auth_router
)

from app.routes.projects import (
    router as projects_router
)

from app.routes.contact import (
    router as contact_router
)

from app.routes.upload import (
    router as upload_router
)

from app.routes.certificates import (
    router as certificates_router
)

from app.routes.resume import (
    router as resume_router
)

from app.routes.hero import (
    router as hero_router
)

from app.routes.skills import (
    router as skills_router
)

from app.routes import about


# Create database tables
Base.metadata.create_all(bind=engine)

tags_metadata = [
    {"name": "Auth"},
    {"name": "Projects"},
    {"name": "Certificates"},
    {"name": "Skills"},
    {"name": "Resume"},
    {"name": "Hero"},
    {"name": "About"},
    {"name": "Contact"}
]



app = FastAPI(
    title="Data Analyst Portfolio API",
    description="Backend API for Data Analyst Portfolio Website",
    version="1.0.0",
    openapi_tags=tags_metadata
)

os.makedirs("uploads", exist_ok=True)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)


# Routers
app.include_router(auth_router)
app.include_router(projects_router)
app.include_router(contact_router)
app.include_router(upload_router)
app.include_router(certificates_router)
app.include_router(skills_router)
app.include_router(resume_router)
app.include_router(hero_router)
app.include_router(about.router)


# CORS
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Root Endpoint
@app.get("/")
def root():

    return {
        "message": "Portfolio API Running",
        "status": "success"
    }

# Health Check Endpoint
@app.get("/api/status")
def status():

    try:

        with engine.connect() as connection:

            connection.execute(
                text("SELECT 1")
            )

        database_status = "connected"

    except Exception as e:

        database_status = "disconnected"

    return {
        "api": "online",
        "database": database_status
    }

