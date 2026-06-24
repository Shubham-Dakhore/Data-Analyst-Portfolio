from pydantic import BaseModel

class HeroCreate(BaseModel):

    full_name: str

    profession: str

    short_bio: str

    linkedin_url: str

    github_url: str

    email: str

    profile_image: str


class HeroResponse(HeroCreate):

    id: int

    class Config:

        from_attributes = True