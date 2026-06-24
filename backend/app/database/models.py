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
from sqlalchemy import Boolean

from sqlalchemy.sql import func

from app.database.connection import Base

# ==========================================
# USERS TABLE
# ==========================================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        index=True,
        nullable=False
    )

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

    technologies = Column(Text)

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

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    issuer = Column(
        String(255),
        nullable=False
    )

    issue_date = Column(
        Date
    )

    credential_id = Column(
        String(255)
    )

    certificate_url = Column(
        String(500)
    )

    image_url = Column(
        String(500)
    )

    description = Column(
        Text
    )

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

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==========================================
# SKILLS TABLE
# ==========================================

class Skill(Base):

    __tablename__ = "skills"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    percentage = Column(
        Integer,
        default=80
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==========================================
# RESUME TABLE
# ==========================================

class Resume(Base):

    __tablename__ = "resumes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    file_name = Column(
        String(255),
        nullable=False
    )

    file_url = Column(
        String(500),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

# ==========================================
# HERO TABLE
# ==========================================

class Hero(Base):

    __tablename__ = "hero"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(255),
        nullable=False
    )

    profession = Column(
        String(255),
        nullable=False
    )

    short_bio = Column(
        Text
    )

    linkedin_url = Column(
        String(500)
    )

    github_url = Column(
        String(500)
    )

    email = Column(
        String(255)
    )

    profile_image = Column(
        String(500)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


# ==========================================
# ABOUT TABLE
# ==========================================

class About(Base):

    __tablename__ = "about"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    location = Column(
        String(255)
    )

    email = Column(
        String(255)
    )

    phone = Column(
        String(20)
    )

    education = Column(
        Text
    )

    summary = Column(
        Text
    )

    journey = Column(
        Text
    )

    image_url = Column(
        String(500)
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )