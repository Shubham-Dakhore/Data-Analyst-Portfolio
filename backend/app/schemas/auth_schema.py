# File: backend/app/schemas/auth_schema.py

from pydantic import BaseModel
from pydantic import EmailStr

# ==========================================
# LOGIN REQUEST
# ==========================================

class LoginRequest(BaseModel):

    email: EmailStr

    password: str

# ==========================================
# LOGIN RESPONSE
# ==========================================

class LoginResponse(BaseModel):

    access_token: str

    token_type: str