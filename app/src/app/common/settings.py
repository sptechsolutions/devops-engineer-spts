from typing import Annotated
from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):

    API_PREFIX: str

    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    CORS_ORIGINS: Annotated[list[str], Field(default_factory=list)]
    CORS_CREDENTIALS: bool = True
    CORS_EXPOSE_HEADERS: Annotated[list[str], Field(default_factory=list)]

    @property
    def db_uri(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
