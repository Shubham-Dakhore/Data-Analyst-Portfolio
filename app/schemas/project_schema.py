# File: backend/app/schemas/project_schema.py

from pydantic import BaseModel
from typing import Optional

# ==========================================
# CREATE PROJECT
# ==========================================

class ProjectCreate(BaseModel):

    title: str

    description: str

    technologies: Optional[str] = None

    github_url: Optional[str] = None

    live_url: Optional[str] = None

    image_url: Optional[str] = None


# ==========================================
# UPDATE PROJECT
# ==========================================

class ProjectUpdate(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    technologies: Optional[str] = None

    github_url: Optional[str] = None

    live_url: Optional[str] = None

    image_url: Optional[str] = None


# ==========================================
# RESPONSE MODEL
# ==========================================

class ProjectResponse(BaseModel):

    id: int

    title: str

    description: str

    technologies: Optional[str]

    github_url: Optional[str]

    live_url: Optional[str]

    image_url: Optional[str]

    class Config:
        from_attributes = True