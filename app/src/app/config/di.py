from plug_in import get_root_config

from app.config.db import db_plugins
from app.config.settings import settings_plugins


def configure() -> None:
    get_root_config().init_root_registry(plugins=[*db_plugins(), *settings_plugins()])
