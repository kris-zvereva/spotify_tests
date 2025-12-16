from dataclasses import dataclass


@dataclass
class Config:
    # Spotify URLs
    OAUTH_URL: str = 'https://accounts.spotify.com'  # For OAuth
    API_BASE_URL: str = 'https://api.spotify.com/v1'  # For API requests
    WEB_URL: str = 'https://open.spotify.com'

    # Browser settings
    driver_name: str = 'chrome'
    timeout: int = 10

    # Scopes (permissions)
    permission_list: str = 'user-library-modify user-library-read playlist-modify-private'

settings = Config()