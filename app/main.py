# File: backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import text

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

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Data Analyst Portfolio API",
    version="1.0.0"
)

# Routers
app.include_router(auth_router)
app.include_router(projects_router)
app.include_router(contact_router)

# CORS
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
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

    except Exception:

        database_status = "disconnected"

    return {
        "api": "online",
        "database": database_status
    }