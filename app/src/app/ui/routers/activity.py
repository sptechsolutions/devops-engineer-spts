from datetime import datetime, timezone
import random
import string
from typing import Annotated, Iterable
from uuid import UUID, uuid4
from fastapi import APIRouter, Body, Depends
from plug_in import get_root_registry
from plug_in.core.host import CoreHost
from pydantic import BaseModel
from sqlalchemy import select

from app.domain.models.activity import Activity
from app.domain.session import SessionMaker


router = APIRouter(prefix="/activity", tags=["Activity"])


@router.post("", status_code=204)
async def create_activity(
    start: Annotated[datetime | None, Body()] = None,
    end: Annotated[datetime | None, Body()] = None,
    session_maker: SessionMaker = Depends(
        lambda: get_root_registry().sync_resolve(CoreHost(SessionMaker))
    ),
) -> None:
    if start is None:
        use_start = datetime.now()
    elif start.tzinfo is None:
        use_start = start.replace(tzinfo=timezone.utc)
    else:
        use_start = start

    if end is None:
        use_end = datetime.now()
    elif end.tzinfo is None:
        use_end = end.replace(tzinfo=timezone.utc)
    else:
        use_end = end

    random_name = "".join(random.choice(string.ascii_uppercase) for _ in range(10))

    activity = Activity(
        id=uuid4(), name=random_name, time_start=use_start, time_end=use_end
    )

    async with session_maker() as session:
        session.add(activity)
        await session.commit()


class ActivityRecord(BaseModel):
    id: UUID
    time_start: datetime
    time_end: datetime | None
    name: str


@router.get("", status_code=200, response_model=list[ActivityRecord])
async def get_activities(
    session_maker: SessionMaker = Depends(
        lambda: get_root_registry().sync_resolve(CoreHost(SessionMaker))
    ),
) -> Iterable[Activity]:

    stmt = select(Activity)

    async with session_maker() as session:
        results = await session.execute(stmt)

    return results.scalars()
