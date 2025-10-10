from fastapi import FastAPI
import uvicorn
from app.config.di import configure
from app.ui.asgi import create_asgi_app


def app_factory() -> FastAPI:
    configure()
    return create_asgi_app()


if __name__ == "__main__":
    uvicorn.run(
        "asgi_dev:app_factory",
        port=8080,
        reload=True,
        access_log=True,
        log_level="debug",
        factory=True,
        host="localhost",
    )
