from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.connect_db.connect_db import get_async_session
from src.course.schema import Course, CourseBase
from src.models import course

router = APIRouter(
    prefix="/course",
    tags=["Course"]
)


@router.get("/", response_model=List[Course])
async def get_course(course_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(course).where(course.c.id == course_id)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        return {
            "status": "error",
            "data": None,
            "detail": error
        }


@router.post("/")
async def add_course(new_course: Course, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(course).values(**new_course.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}

    except Exception as error:
        return {
            "status": "error",
            "data": None,
            "detail": error
        }


@router.put("/")
async def change_course(course_id: int, new_course: CourseBase, session: AsyncSession = Depends(get_async_session)):
    try:
        values = {**new_course.dict()}
        values.pop("id", None)
        stmt = course.update().where(course.c.id == course_id).values(values)
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception as error:
        return {
            "status": "error",
            "data": None,
            "detail": error
        }


@router.delete("/")
async def delete_course(course_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = course.delete().where(course.c.id == course_id)
        await session.execute(query)
        await session.commit()
        return {"status": "delete"}
    except Exception as error:
        return {
            "status": "error",
            "data": None,
            "detail": error
        }
