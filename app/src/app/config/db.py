from sqlalchemy.ext.asyncio import AsyncEngine

from plug_in import plug
from plug_in.types.proto.core_plugin import CorePluginProtocol

from app.domain.session import SessionMaker
from app.infra.session import session_context_maker, async_engine_maker


def db_plugins() -> list[CorePluginProtocol]:

    return [
        plug(async_engine_maker).into(AsyncEngine).via_provider("lazy"),
        plug(session_context_maker).into(SessionMaker).via_provider("lazy"),
    ]
