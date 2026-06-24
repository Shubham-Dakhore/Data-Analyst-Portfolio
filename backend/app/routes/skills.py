from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models import Skill

from app.schemas.skill_schema import (
    SkillCreate,
    SkillUpdate,
    SkillResponse
)

router = APIRouter(
    prefix="/api/skills",
    tags=["Skills"]
)

@router.get(
    "/",
    response_model=list[SkillResponse]
)
def get_skills(
    db: Session = Depends(get_db)
):
    return db.query(Skill).all()

@router.get(
    "/{skill_id}",
    response_model=SkillResponse
)
def get_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):

    skill = (
        db.query(Skill)
        .filter(
            Skill.id == skill_id
        )
        .first()
    )

    if not skill:

        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    return skill

@router.post(
    "/",
    response_model=SkillResponse
)
def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db)
):

    new_skill = Skill(
        **skill.model_dump()
    )

    db.add(new_skill)

    db.commit()

    db.refresh(new_skill)

    return new_skill


@router.put(
    "/{skill_id}",
    response_model=SkillResponse
)
def update_skill(
    skill_id: int,
    skill_data: SkillUpdate,
    db: Session = Depends(get_db)
):

    skill = (
        db.query(Skill)
        .filter(
            Skill.id == skill_id
        )
        .first()
    )

    if not skill:

        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    for key, value in skill_data.model_dump(
        exclude_unset=True
    ).items():

        setattr(
            skill,
            key,
            value
        )

    db.commit()

    db.refresh(skill)

    return skill


@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):

    skill = (
        db.query(Skill)
        .filter(
            Skill.id == skill_id
        )
        .first()
    )

    if not skill:

        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    db.delete(skill)

    db.commit()

    return {
        "message":
        "Skill deleted"
    }