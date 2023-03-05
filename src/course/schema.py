from typing import Optional

from pydantic import BaseModel


class CourseBase(BaseModel):
    name: str


class Course(CourseBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
