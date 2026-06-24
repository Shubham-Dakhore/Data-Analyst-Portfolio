# File: backend/app/utils/jwt_handler.py

import os

from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from dotenv import load_dotenv

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)

if not SECRET_KEY:
    raise ValueError(
        "SECRET_KEY is missing"
    )

ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        60
    )
)

# ==========================================
# CREATE TOKEN
# ==========================================

def create_access_token(
    data: dict
):

    payload = data.copy()

    expire = (
        datetime.now()
        + timedelta(
            minutes=
            ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload.update(
        {
            "exp": expire
        }
    )

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

# ==========================================
# VERIFY TOKEN
# ==========================================

def verify_token(
    token: str
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None
    