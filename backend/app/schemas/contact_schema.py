# File: backend/app/schemas/contact_schema.py

from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime

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

    is_read: int

    created_at: datetime

    class Config:
        from_attributes = True
    