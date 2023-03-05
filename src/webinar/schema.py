from enum import Enum
from typing import Optional

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


class WebinarBase(BaseModel):
    course: int
    teacher: int
    status: StatusEnum


class Webinar(WebinarBase):
    id: Optional[int] = None
    name: str
    email: str

    class Config:
        orm_mode = True


class WebinarCreate(WebinarBase):
    id: int
