from contextlib import asynccontextmanager
from click import echo
from plug_in import Hosted, manage

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine

from app.common.settings import AppSettings
from app.domain.session import SessionMaker


@manage()
def async_engine_maker(settings: AppSettings = Hosted()) -> AsyncEngine:
    return create_async_engine(settings.db_uri, echo=True)


@manage()
def session_context_maker(engine: AsyncEngine = Hosted()) -> SessionMaker:
    sm = async_sessionmaker(
        engine,
        autoflush=False,
        expire_on_commit=False,
    )

    @asynccontextmanager
    async def create_sm():
        async with sm() as s:
            yield s

    return create_sm
