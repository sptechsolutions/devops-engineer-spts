from plug_in import plug
from plug_in.types.proto.core_plugin import CorePluginProtocol
from pathlib import Path

from app.common.settings import AppSettings


def settings_plugins() -> list[CorePluginProtocol]:
    return [
        plug(provide_settings()).into(AppSettings).directly(),
    ]


def provide_settings() -> AppSettings:
    # Get the repo root directory (4 levels up from this file)
    repo_root = Path(__file__).parent.parent.parent.parent
    env_file_path = repo_root / ".env"

    return AppSettings(_env_file=env_file_path)  # type: ignore
