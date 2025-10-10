from typing import Protocol, Self
from sqlalchemy.ext.asyncio import AsyncSession
import types


class SessionContext(Protocol):

    async def __aenter__(self) -> AsyncSession: ...

    async def __aexit__(
        self,
        typ: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> bool | None: ...


class SessionMaker(Protocol):

    def __call__(self) -> SessionContext: ...
