from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.database.models import About

from app.schemas.about_schema import (
    AboutCreate,
    AboutResponse
)

router = APIRouter(
    prefix="/api/about",
    tags=["About"]
)


# ==========================================
# GET ABOUT
# ==========================================

@router.get(
    "/",
    response_model=list[AboutResponse]
)
def get_about(
    db: Session = Depends(get_db)
):

    return (
        db.query(About)
        .order_by(About.id.desc())
        .limit(1)
        .all()
    )


# ==========================================
# SAVE ABOUT
# ==========================================

@router.post(
    "/",
    response_model=AboutResponse
)
def create_about(
    about_data: AboutCreate,
    db: Session = Depends(get_db)
):

    old_about = (
        db.query(About)
        .first()
    )

    if old_about:

        db.delete(old_about)

        db.commit()

    about = About(

        location=about_data.location,

        email=about_data.email,

        phone=about_data.phone,

        education=about_data.education,

        summary=about_data.summary,

        journey=about_data.journey,

        image_url = about_data.image_url
    )

    db.add(about)

    db.commit()

    db.refresh(about)

    return about

    