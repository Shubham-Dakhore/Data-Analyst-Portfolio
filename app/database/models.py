# File: backend/app/database/models.py

"""
Database Models
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Date
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from app.database.connection import Base

# ==========================================
# USERS TABLE
# ==========================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==========================================
# PROJECTS TABLE
# ==========================================

class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    description = Column(Text, nullable=False)

    technologies = Column(String(255))

    github_url = Column(String(255))

    live_url = Column(String(255))

    image_url = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==========================================
# CERTIFICATIONS TABLE
# ==========================================

class Certification(Base):

    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    issuer = Column(String(255))

    issue_date = Column(Date)

    certificate_url = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==========================================
# CONTACTS TABLE
# ==========================================

class Contact(Base):

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    email = Column(String(150), nullable=False)

    subject = Column(String(255), nullable=False)

    message = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    