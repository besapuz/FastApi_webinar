from typing import List

from fastapi import APIRouter, Depends
from loguru import logger
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.connect_db.connect_db import get_async_session
from src.models import webinar, teacher
from src.webinar.schema import Webinar, StatusEnum, WebinarCreate, WebinarBase

router = APIRouter(
    prefix="/webinar",
    tags=["Webinar"]
)


@router.get("/", response_model=List[Webinar])
async def get_webinar(status: StatusEnum, session: AsyncSession = Depends(get_async_session)):
    query = \
        select(webinar, teacher).\
        where(webinar.c.status == status).\
        join(teacher, teacher.c.webinar_id == webinar.c.teacher).\
        where(teacher.c.webinar_id == webinar.c.teacher)
    result = await session.execute(query)
    logger.info(result.all())
    await session.close()
    return result.all()


@router.post("/")
async def add_webinar(new_webinar: WebinarCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(webinar).values(**new_webinar.dict())
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
async def change_webinar(web_id: int, new_webinar: WebinarBase, session: AsyncSession = Depends(get_async_session)):
    try:
        values = {**new_webinar.dict()}
        values.pop("id", None)
        stmt = webinar.update().where(webinar.c.id == web_id).values(values)
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
async def delete_webinar(web_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = webinar.delete().where(webinar.c.id == web_id)
        await session.execute(query)
        await session.commit()
        return {"status": "delete"}
    except Exception as error:
        return {
            "status": "error",
            "data": None,
            "detail": error
        }
