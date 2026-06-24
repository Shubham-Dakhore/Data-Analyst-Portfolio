# File: backend/app/routes/auth.py

from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.auth_schema import (
    LoginRequest,
    LoginResponse
)

from app.utils.jwt_handler import (
    create_access_token
)

from app.utils.password import (
    verify_password
)

router = APIRouter(
    prefix="/api",
    tags=["Authentication"]
)

# ==========================================
# DEMO ADMIN USER
# ==========================================
# Later this will come from MySQL

DEMO_ADMIN = {

    "email":
        "admin@email.com",

    # plain password for demo only
    "password":
        "admin123"
}

# ==========================================
# LOGIN API
# ==========================================

@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    credentials: LoginRequest
):

    if (
        credentials.email
        != DEMO_ADMIN["email"]
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if (
        credentials.password
        != DEMO_ADMIN["password"]
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub":
            credentials.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# ==========================================
# PROTECTED TEST ROUTE
# ==========================================

@router.get(
    "/protected"
)
def protected_route():

    return {
        "message":
        "Protected route working"
    }