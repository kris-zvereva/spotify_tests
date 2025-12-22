from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv


load_dotenv()


class MobileConfig(BaseSettings):
    """Mobile test configuration"""

    remote_url: str

    # Android capabilities
    platform_name: str = 'Android'
    platform_version: str
    device_name: str
    automation_name: str = 'UiAutomator2'

    # Spotify app
    app_package: str = 'com.spotify.music'
    app_activity: str = '.MainActivity'
    app: str  # Путь к APK или bs://id

    # Settings
    no_reset: bool = True
    timeout: int = 20

    # BrowserStack specific
    bstack_project: str = 'Spotify_Mobile_Tests'
    bstack_build: str = 'Android_Signup'

    model_config = SettingsConfigDict(
        env_file=('.env.mobile.bstack', '.env.mobile.local'),
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

    # BrowserStack capabilities if remote
    context = os.getenv('MOBILE_CONTEXT', 'remote')
    if context == 'remote':
        options.app = config.app
        options.set_capability('bstack:options', {
            'projectName': config.bstack_project,
            'buildName': config.bstack_build,
            'userName': os.getenv('browserstack_username'),
            'accessKey': os.getenv('browserstack_access_key'),
        })
    else:
        app_path = Path(__file__).parent / config.app
        options.app = str(app_path.absolute())
        options.no_reset = config.no_reset

    return options


context = os.getenv('MOBILE_CONTEXT', 'remote')
if context == 'remote':
    mobile_settings = MobileConfig(_env_file='.env.mobile.bstack')
else:
    mobile_settings = MobileConfig(_env_file='.env.mobile.local')