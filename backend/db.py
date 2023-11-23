from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import AsyncIterator

engine = create_async_engine("sqlite+aiosqlite:///work.db")
async_session = async_sessionmaker(engine, class_=AsyncSession)


async def get_db() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session
