# File: backend/app/schemas/project_schema.py

from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import Field
from typing import Optional
from pydantic import ConfigDict

model_config = ConfigDict(
    from_attributes=True
)

# ==========================================
# CREATE PROJECT
# ==========================================

class ProjectCreate(BaseModel):

    title: str = Field(
        ...,
        min_length=3,
        max_length=150
    )

    description: str = Field(
        ...,
        min_length=20,
        max_length=3000
    )

    technologies: Optional[str] = Field(
        None,
        max_length=500
    )

    github_url: Optional[HttpUrl] = None

    live_url: Optional[HttpUrl] = None

    image_url: Optional[str] = None


# ==========================================
# UPDATE PROJECT
# ==========================================

class ProjectUpdate(BaseModel):

    title: Optional[str] = Field(
        None,
        min_length=3,
        max_length=150
    )

    description: Optional[str] = Field(
        None,
        min_length=20,
        max_length=3000
    )

    technologies: Optional[str] = Field(
        None,
        max_length=500
    )

    github_url: Optional[HttpUrl] = None

    live_url: Optional[HttpUrl] = None

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

    