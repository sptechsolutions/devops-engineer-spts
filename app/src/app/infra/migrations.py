import asyncio
from plug_in import Hosted, manage
from app.domain.models.activity import Base

from sqlalchemy.ext.asyncio import AsyncEngine


@manage()
async def ensure_all_tables_exists(engine: AsyncEngine = Hosted()) -> None:
    """
    Poorly created migration routine, will fork for showcasing
    """

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all, checkfirst=True)
