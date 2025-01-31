from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    async_sessionmaker,
    AsyncSession,
    create_async_engine,
)

engine = create_async_engine(url='sqlite+aiosqlite:///database.db')

async_session = async_sessionmaker(engine, class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(Integer)
    fullname: Mapped[str] = mapped_column(String(50), nullable=True)
    username: Mapped[str] = mapped_column(String(50), nullable=True)
    time_register: Mapped[str] = mapped_column(String(50), nullable=True)
    time_last: Mapped[str] = mapped_column(String(50), nullable=True)
    action_last: Mapped[str] = mapped_column(String(50), nullable=True)
    count: Mapped[int] = mapped_column(nullable=True)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
