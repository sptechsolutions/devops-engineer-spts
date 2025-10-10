from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from plug_in import Hosted, manage

from app.common.settings import AppSettings
from app.infra.migrations import ensure_all_tables_exists
from app.ui.routers.activity import router as activity_router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    await ensure_all_tables_exists()
    yield None


@manage()
def create_asgi_app(settings: AppSettings = Hosted()) -> FastAPI:
    app = FastAPI(root_path=settings.API_PREFIX, lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_CREDENTIALS,
        expose_headers=settings.CORS_EXPOSE_HEADERS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(activity_router)
    return app
