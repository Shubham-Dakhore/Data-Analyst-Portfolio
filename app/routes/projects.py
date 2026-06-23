# File: backend/app/routes/projects.py

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.database.models import Project

from app.schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)

router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)

# ==========================================
# GET ALL PROJECTS
# ==========================================

@router.get(
    "/",
    response_model=list[ProjectResponse]
)
def get_projects(
    db: Session = Depends(get_db)
):

    projects = db.query(Project).all()

    return projects


# ==========================================
# GET PROJECT BY ID
# ==========================================

@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


# ==========================================
# CREATE PROJECT
# ==========================================

@router.post(
    "/",
    response_model=ProjectResponse
)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db)
):

    project = Project(

        title=project_data.title,

        description=project_data.description,

        technologies=project_data.technologies,

        github_url=project_data.github_url,

        live_url=project_data.live_url,

        image_url=project_data.image_url
    )

    db.add(project)

    db.commit()

    db.refresh(project)

    return project


# ==========================================
# UPDATE PROJECT
# ==========================================

@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db)
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    update_data = (
        project_data.model_dump(
            exclude_unset=True
        )
    )

    for key, value in update_data.items():

        setattr(
            project,
            key,
            value
        )

    db.commit()

    db.refresh(project)

    return project


# ==========================================
# DELETE PROJECT
# ==========================================

@router.delete(
    "/{project_id}"
)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)

    db.commit()

    return {
        "message":
        "Project deleted successfully"
    }