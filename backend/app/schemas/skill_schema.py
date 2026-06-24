from pydantic import BaseModel

class SkillCreate(BaseModel):

    name: str

    percentage: int


class SkillUpdate(BaseModel):

    name: str | None = None

    percentage: int | None = None


class SkillResponse(BaseModel):

    id: int

    name: str

    percentage: int

    class Config:
        from_attributes = True

