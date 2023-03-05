from typing import Optional

from pydantic import BaseModel


class Course(BaseModel):
    id: Optional[int] = None
    name: str

    class Config:
        orm_mode = True
