from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
import os

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.database.models import Certification

from app.schemas.certificate_schema import (
    CertificateCreate,
    CertificateUpdate,
    CertificateResponse
)

router = APIRouter(
    prefix="/api/certificates",
    tags=["Certificates"]
)


# ==========================================
# GET ALL CERTIFICATES
# ==========================================

@router.get(
    "/",
    response_model=list[CertificateResponse]
)
def get_certificates(
    db: Session = Depends(get_db)
):

    certificates = (
        db.query(Certification)
        .order_by(Certification.id.desc())
        .all()
    )

    return certificates


# ==========================================
# GET CERTIFICATE BY ID
# ==========================================

@router.get(
    "/{certificate_id}",
    response_model=CertificateResponse
)
def get_certificate(
    certificate_id: int,
    db: Session = Depends(get_db)
):

    certificate = (
        db.query(Certification)
        .filter(
            Certification.id == certificate_id
        )
        .first()
    )

    if not certificate:

        raise HTTPException(
            status_code=404,
            detail="Certificate not found"
        )

    return certificate


# ==========================================
# CREATE CERTIFICATE
# ==========================================

@router.post(
    "/",
    response_model=CertificateResponse
)
def create_certificate(
    certificate_data: CertificateCreate,
    db: Session = Depends(get_db)
):

    certificate = Certification(
        **certificate_data.model_dump()
    )

    db.add(certificate)

    db.commit()

    db.refresh(certificate)

    return certificate


# ==========================================
# UPDATE CERTIFICATE
# ==========================================

@router.put(
    "/{certificate_id}",
    response_model=CertificateResponse
)
def update_certificate(
    certificate_id: int,
    certificate_data: CertificateUpdate,
    db: Session = Depends(get_db)
):

    certificate = (
        db.query(Certification)
        .filter(
            Certification.id == certificate_id
        )
        .first()
    )

    if not certificate:

        raise HTTPException(
            status_code=404,
            detail="Certificate not found"
        )

    update_data = (
        certificate_data.model_dump(
            exclude_unset=True
        )
    )

    for key, value in update_data.items():

        setattr(
            certificate,
            key,
            value
        )

    db.commit()

    db.refresh(certificate)

    return certificate


# ==========================================
# DELETE CERTIFICATE
# ==========================================

@router.delete(
    "/{certificate_id}"
)
def delete_certificate(
    certificate_id: int,
    db: Session = Depends(get_db)
):

    certificate = (
        db.query(Certification)
        .filter(
            Certification.id == certificate_id
        )
        .first()
    )

    if not certificate:

        raise HTTPException(
            status_code=404,
            detail="Certificate not found"
        )
    

    if certificate.image_url:

        image_path = certificate.image_url.replace("/uploads/", "uploads/")

        if os.path.exists(image_path):
            os.remove(image_path)
    

    try:

        db.commit()

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database error"
        )