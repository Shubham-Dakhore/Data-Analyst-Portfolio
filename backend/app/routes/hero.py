from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.database.models import Hero

from app.schemas.hero_schema import (
    HeroCreate,
    HeroResponse
)

router = APIRouter(
    prefix="/api/hero",
    tags=["Hero"]
)


@router.get(
    "/",
    response_model=list[HeroResponse]
)
def get_hero(
    db: Session = Depends(get_db)
):

    return db.query(Hero).all()


@router.post(
    "/",
    response_model=HeroResponse
)
def create_hero(
    hero: HeroCreate,
    db: Session = Depends(get_db)
):

    db.query(Hero).delete()

    db.commit()

    new_hero = Hero(
        **hero.model_dump()
    )

    db.add(new_hero)

    db.commit()

    db.refresh(new_hero)

    return new_hero