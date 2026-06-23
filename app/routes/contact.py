# File: backend/app/routes/contact.py

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.database.models import Contact

from app.schemas.contact_schema import (
    ContactCreate,
    ContactResponse
)

router = APIRouter(
    prefix="/api",
    tags=["Contact"]
)

# ==========================================
# SUBMIT CONTACT FORM
# ==========================================

@router.post(
    "/contact",
    response_model=ContactResponse
)
def submit_contact(
    contact_data: ContactCreate,
    db: Session = Depends(get_db)
):

    contact = Contact(

        name=contact_data.name,

        email=contact_data.email,

        subject=contact_data.subject,

        message=contact_data.message
    )

    db.add(contact)

    db.commit()

    db.refresh(contact)

    return contact


# ==========================================
# GET ALL MESSAGES
# ==========================================

@router.get(
    "/messages",
    response_model=list[ContactResponse]
)
def get_messages(
    db: Session = Depends(get_db)
):

    messages = (
        db.query(Contact)
        .order_by(Contact.id.desc())
        .all()
    )

    return messages