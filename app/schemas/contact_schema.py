# File: backend/app/schemas/contact_schema.py

from pydantic import BaseModel
from pydantic import EmailStr

# ==========================================
# CONTACT CREATE
# ==========================================

class ContactCreate(BaseModel):

    name: str

    email: EmailStr

    subject: str

    message: str


# ==========================================
# CONTACT RESPONSE
# ==========================================

class ContactResponse(BaseModel):

    id: int

    name: str

    email: str

    subject: str

    message: str

    class Config:
        from_attributes = True