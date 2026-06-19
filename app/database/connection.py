# File: backend/app/database/connection.py

"""
Database Connection Configuration
"""

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# ==========================================
# DATABASE URL
# ==========================================

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================
# SQLALCHEMY ENGINE
# ==========================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# ==========================================
# SESSION FACTORY
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ==========================================
# BASE MODEL
# ==========================================

Base = declarative_base()

# ==========================================
# DATABASE DEPENDENCY
# ==========================================

def get_db():
    """
    Dependency Injection
    for FastAPI Routes
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()