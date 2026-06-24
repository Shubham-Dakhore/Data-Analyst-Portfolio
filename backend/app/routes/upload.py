from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

import os
import shutil
import uuid


router = APIRouter(
    prefix="/api/upload",
    tags=["Upload"]
)

# ==========================================
# UPLOAD FOLDERS
# ==========================================

PROJECT_UPLOAD_DIR = "uploads/projects"

CERTIFICATE_UPLOAD_DIR = "uploads/certificates"

os.makedirs(
    PROJECT_UPLOAD_DIR,
    exist_ok=True
)

os.makedirs(
    CERTIFICATE_UPLOAD_DIR,
    exist_ok=True
)


RESUME_DIRECTORY = "uploads/resume"

os.makedirs(
    RESUME_DIRECTORY,
    exist_ok=True
)

HERO_DIRECTORY = "uploads/hero"

os.makedirs(
    HERO_DIRECTORY,
    exist_ok=True
)

ABOUT_DIRECTORY = "uploads/about"

os.makedirs(
    ABOUT_DIRECTORY,
    exist_ok=True
)

# ==========================================
# VALIDATE IMAGE
# ==========================================

def validate_image(filename):

    allowed_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp"
    ]

    extension = os.path.splitext(
        filename
    )[1].lower()

    if extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Invalid image format"
        )

    return extension


# ==========================================
# PROJECT IMAGE UPLOAD
# ==========================================

@router.post("/project-image")
async def upload_project_image(

    image: UploadFile = File(...)

):

    extension = validate_image(
        image.filename
    )

    unique_filename = (
        f"{uuid.uuid4()}{extension}"
    )

    file_path = os.path.join(
        PROJECT_UPLOAD_DIR,
        unique_filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            image.file,
            buffer
        )

    return {

        "image_url":
        f"/uploads/projects/{unique_filename}"

    }


# ==========================================
# CERTIFICATE IMAGE UPLOAD
# ==========================================

@router.post("/certificate-image")
async def upload_certificate_image(

    image: UploadFile = File(...)

):

    extension = validate_image(
        image.filename
    )

    unique_filename = (
        f"{uuid.uuid4()}{extension}"
    )

    file_path = os.path.join(
        CERTIFICATE_UPLOAD_DIR,
        unique_filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            image.file,
            buffer
        )

    return {

        "image_url":
        f"/uploads/certificates/{unique_filename}"

    }


@router.post("/resume")
async def upload_resume(

    file: UploadFile = File(...)

):

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension != ".pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF allowed"
        )

    filename = (
        f"{uuid.uuid4()}{extension}"
    )

    filepath = os.path.join(
        RESUME_DIRECTORY,
        filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {

        "file_name":
        file.filename,

        "file_url":
        f"/uploads/resume/{filename}"
    }



# ==========================================
# HERO IMAGE UPLOAD
# ==========================================

@router.post("/hero-image")
async def upload_hero_image(

    image: UploadFile = File(...)

):

    extension = validate_image(
        image.filename
    )

    filename = (
        f"{uuid.uuid4()}{extension}"
    )

    filepath = os.path.join(
        HERO_DIRECTORY,
        filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            image.file,
            buffer
        )

    return {

        "image_url":
        f"/uploads/hero/{filename}"

    }

# ==========================================
# ABOUT IMAGE UPLOAD
# ==========================================

@router.post("/about-image")
async def upload_about_image(

    image: UploadFile = File(...)

):

    extension = validate_image(
        image.filename
    )

    filename = (
        f"{uuid.uuid4()}{extension}"
    )

    filepath = os.path.join(
        ABOUT_DIRECTORY,
        filename
    )

    with open(
        filepath,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            image.file,
            buffer
        )

    return {

        "image_url":
        f"/uploads/about/{filename}"

    }