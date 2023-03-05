
from typing import AsyncGenerator

import databases
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from src.config import InitialData

initial = InitialData()
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{initial.DB_USER}:{initial.DB_PASS}@{initial.DB_HOST}:{initial.DB_PORT}/{initial.DB_NAME}"

Base = declarative_base()

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
