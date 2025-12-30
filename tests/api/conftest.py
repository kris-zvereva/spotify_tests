import base64
import logging
import os
import random
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlencode

import pytest
import requests
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver

from api_clients.auth_helper import SpotifyAuthHelper
from api_clients.playlist_client import PlaylistClient
from api_clients.search_client import SearchClient
from api_clients.track_client import TrackClient
from config import settings

env_path = Path(__file__).resolve().parents[2] / ".env.api"
load_dotenv(env_path)


@dataclass
class TestAccount:
    name: str
    email: str
    id: str
    password: str


def get_random_test_account() -> TestAccount:
    """Returns random test account credentials"""
    account_count = 0
    for i in range(1, 20):
        if not os.getenv(f"user{i}_email"):
            break
        account_count = i

    if account_count == 0:
        raise ValueError("No test accounts found in environment variables!")

    random_i = random.randint(1, account_count)
    return TestAccount(
        name=os.getenv(f"user{random_i}_name"),
        email=os.getenv(f"user{random_i}_email"),
        id=os.getenv(f"user{random_i}_id"),
        password=os.getenv(f"user{random_i}_password"),
    )


@pytest.fixture(scope="session")
def test_account():
    """Get random test account for session"""
    return get_random_test_account()


@pytest.fixture(scope="session")
def client_credentials_token():
    """
    Token for PUBLIC endpoints (search, tracks info).
    Without browser authorization.
    """
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")

    assert client_id, "client_id not set!"
    assert client_secret, "client_secret not set!"

    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode("utf-8")

    response = requests.post(
        f"{settings.OAUTH_URL}/api/token",
        headers={
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"grant_type": "client_credentials"},
    )

    assert response.status_code == 200, f"Failed to get token: {response.text}"

    return {"Authorization": f"Bearer {response.json()['access_token']}"}


@pytest.fixture(scope="session")
def setup_browser():
    """Browser setup for OAuth flow"""
    browser.config.base_url = settings.OAUTH_URL
    browser.config.driver_name = settings.driver_name
    browser.config.timeout = settings.timeout

    # Chrome options для Jenkins (headless)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")

    browser.config.driver_options = options

    yield

    # browser.quit()
    try:
        if hasattr(browser, "driver") and browser.driver:
            browser.quit()
    except Exception as e:
        logging.warning(f"Browser cleanup error (can be ignored): {e}")


@pytest.fixture(scope="session")
def user_auth_token(setup_browser, test_account):
    """
    Token for USER endpoints (favorites, playlists).
    requires browser authorization
    """
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    user_mail = test_account.email
    user_password = test_account.password
    callback_url = os.getenv("callback_url")

    # Authorization request
    auth_params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": callback_url,
        "scope": settings.permission_list,
    }

    browser.open("/authorize?" + urlencode(auth_params))

    # get auth code via browser
    authorization_code = SpotifyAuthHelper.authorize_and_get_code(
        user_mail, user_password
    )

    # exchange code for access token
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode("utf-8")

    token_response = requests.post(
        f"{settings.OAUTH_URL}/api/token",
        headers={
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": authorization_code,
            "redirect_uri": callback_url,
        },
    )

    assert (
        token_response.status_code == 200
    ), f"Token exchange failed: {token_response.text}"

    return {
        "Authorization": f"Bearer {token_response.json()['access_token']}",
        "user_id": test_account.id,
    }


@pytest.fixture(scope="session")
def search_client(client_credentials_token):
    """Search client for public endpoints"""
    return SearchClient(client_credentials_token)


@pytest.fixture(scope="session")
def track_client(client_credentials_token):
    """Track client for public endpoints"""
    return TrackClient(client_credentials_token)


@pytest.fixture(scope="session")
def user_track_client(user_auth_token):
    """Track client for user endpoints"""
    auth_header = {"Authorization": user_auth_token["Authorization"]}
    return TrackClient(auth_header)


@pytest.fixture(scope="session")
def playlist_client(user_auth_token):
    """Playlist client for user endpoints"""
    auth_header = {"Authorization": user_auth_token["Authorization"]}
    return PlaylistClient(auth_header)


@pytest.fixture(scope="session")
def user_id(user_auth_token):
    """Extract user_id from auth token fixture"""
    return user_auth_token["user_id"]
