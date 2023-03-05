from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


# class Teacher(BaseModel):
#     id: int
#     email: str
#     name: str
#     webinar_id: int

class StatusEnum(str, Enum):
    CANCEL = 'отменен'
    IN_WORK = 'сейчас идет'
    END = 'закончен'
    GENERATED = 'создан'


class WebinarCreate(BaseModel):
    id: Optional[int] = None
    course: int
    teacher: int
    status: StatusEnum

    class Config:
        orm_mode = True

