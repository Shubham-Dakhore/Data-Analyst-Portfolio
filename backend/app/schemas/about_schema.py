from pydantic import BaseModel
from typing import Optional


class AboutBase(BaseModel):

    location: str | None = None

    email: str | None = None

    phone: str | None = None

    education: str | None = None

    summary: str | None = None

    journey: str | None = None

    image_url: Optional[str] = None



class AboutCreate(AboutBase):
    pass


class AboutResponse(BaseModel):

    id: int
    location: str
    email: str
    phone: str
    education: str
    summary: str
    journey: str

    image_url: Optional[str] = None

    class Config:
        from_attributes = True