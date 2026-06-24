# File: backend/app/database/connection.py

"""
Database Connection Configuration
"""

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import Session

from urllib.parse import quote_plus

DB_PASSWORD = quote_plus(
    os.getenv("DB_PASSWORD") or ""
)

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


if not all([
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
]):
    raise ValueError(
        "Database environment variables are missing"
    )

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
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    pool_recycle=3600
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

def get_db() -> Session:
    """
    Provides a database session
    for each request and ensures
    it is properly closed.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()