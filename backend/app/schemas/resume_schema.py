from pydantic import BaseModel

class ResumeResponse(BaseModel):

    id: int

    file_name: str

    file_url: str

    class Config:
        from_attributes = True


class ResumeCreate(BaseModel):

    file_name: str

    file_url: str