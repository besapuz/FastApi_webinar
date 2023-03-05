import asyncio
from typing import List


from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from loguru import logger
from src.connect_db.connect_db import get_async_session
from src.models import webinar, teacher
from src.webinar.schema import WebinarCreate, StatusEnum

router = APIRouter(
    prefix="/webinar",
    tags=["Webinar"]
)


@router.get("/", response_model=List[WebinarCreate])
async def get_webinar(status: StatusEnum, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(webinar).where(webinar.c.status == status)
        result = await session.execute(query)
        return result.all()
    except Exception as error:
        return {
            "status": "error",
            "data": None,
            "detail": error
        }


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
async def change_webinar(web_id: int, new_webinar: WebinarCreate, session: AsyncSession = Depends(get_async_session)):
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



