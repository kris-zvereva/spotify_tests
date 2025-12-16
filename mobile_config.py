from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, Optional
from appium.options.android import UiAutomator2Options
import os


class MobileConfig(BaseSettings):
    """Mobile test configuration"""

    context: Literal['local', 'remote'] = 'local'

    # Appium/BrowserStack URL
    remote_url: str

    # Common Android capabilities
    platform_name: str = 'Android'
    platform_version: str
    device_name: str
    automation_name: str = 'UiAutomator2'

    # Spotify app
    app_package: str = 'com.spotify.music'
    app_activity: str = '.MainActivity'
    app: str  # Путь или bs://id

    # Settings
    no_reset: bool = True
    timeout: int = 20

    # BrowserStack specific
    bstack_username: Optional[str] = None
    bstack_access_key: Optional[str] = None
    bstack_project: str = 'Spotify_Mobile_Tests'
    bstack_build: str = 'Android_Signup'
    bstack_session: str = 'Signup_Flow'

    model_config = SettingsConfigDict(
        env_file=('.env', f'.env.mobile.{os.getenv("MOBILE_CONTEXT", "local")}'),
        env_file_encoding='utf-8',
        env_prefix='MOBILE_',
        case_sensitive=False,
        extra='ignore'
    )


def to_driver_options(config: MobileConfig) -> UiAutomator2Options:
    """Convert config to Appium options"""
    options = UiAutomator2Options()

    options.platform_name = config.platform_name
    options.platform_version = config.platform_version
    options.device_name = config.device_name
    options.automation_name = config.automation_name
    options.app_package = config.app_package
    options.app_activity = config.app_activity

    if config.context == 'local':
        options.app = os.path.abspath(config.app)
        options.no_reset = config.no_reset

    elif config.context == 'remote':
        options.app = config.app  # bs://...
        options.set_capability('bstack:options', {
            'projectName': config.bstack_project,
            'buildName': config.bstack_build,
            'sessionName': config.bstack_session,
            'userName': config.bstack_username,
            'accessKey': config.bstack_access_key,
        })

    return options


mobile_settings = MobileConfig()