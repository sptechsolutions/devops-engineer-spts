from app.config.di import configure
from app.ui.asgi import create_asgi_app


configure()

app = create_asgi_app()
