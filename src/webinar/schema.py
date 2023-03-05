from typing import Optional

from pydantic import BaseModel


class WebinarCreate(BaseModel):
    id: Optional[int] = None
    course: int
    teacher: int
    status: str

    class Config:
        orm_mode = True
