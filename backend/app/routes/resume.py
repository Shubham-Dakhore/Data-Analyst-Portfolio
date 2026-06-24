from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.database.models import Resume

from app.schemas.resume_schema import ResumeResponse

from app.schemas.resume_schema import ResumeCreate

router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"]
)

@router.get(
    "/",
    response_model=list[ResumeResponse]
)
def get_resume(
    db: Session = Depends(get_db)
):

    return (

        db.query(Resume)

        .order_by(
            Resume.id.desc()
        )

        .limit(1)

        .all()
    )


@router.post(
    "/",
    response_model=ResumeResponse
)

def create_resume(

    resume: ResumeCreate,

    db: Session = Depends(get_db)

):

    new_resume = Resume(

        file_name=resume.file_name,

        file_url=resume.file_url

    )

    db.add(new_resume)

    db.commit()

    db.refresh(new_resume)

    return new_resume

