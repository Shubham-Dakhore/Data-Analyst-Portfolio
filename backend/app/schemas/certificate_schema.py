from pydantic import BaseModel
from typing import Optional
from datetime import date


class CertificateCreate(BaseModel):

    title: str

    issuer: str

    issue_date: Optional[date] = None

    credential_id: Optional[str] = None

    certificate_url: Optional[str] = None

    image_url: Optional[str] = None

    description: Optional[str] = None


class CertificateUpdate(BaseModel):

    title: Optional[str] = None

    issuer: Optional[str] = None

    issue_date: Optional[date] = None

    credential_id: Optional[str] = None

    certificate_url: Optional[str] = None

    image_url: Optional[str] = None

    description: Optional[str] = None


class CertificateResponse(BaseModel):

    id: int

    title: str

    issuer: str

    issue_date: Optional[date]

    credential_id: Optional[str]

    certificate_url: Optional[str]

    image_url: Optional[str]

    description: Optional[str]

    class Config:

        from_attributes = True