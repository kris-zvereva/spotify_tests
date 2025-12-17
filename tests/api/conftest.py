import sys
from pathlib import Path
from selenium.common import NoSuchElementException, TimeoutException

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import os
import time
import base64
import logging
from urllib.parse import urlencode
import requests
import pytest
from selene.support.shared import browser
from selene import be, command
from selenium import webdriver
from dotenv import load_dotenv

from api_clients.playlist_client import PlaylistClient
from api_clients.search_client import SearchClient
from api_clients.track_client import TrackClient
from config import settings

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


@pytest.fixture(scope='session')
def client_credentials_token():
    """
    Token for PUBLIC endpoints (search, tracks info).
    Without browser authorization.
    """
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')

    assert client_id, "client_id not set!"
    assert client_secret, "client_secret not set!"

    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode('utf-8')

    response = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={'grant_type': 'client_credentials'}
    )

    assert response.status_code == 200, f"Failed to get token: {response.text}"

    return {
        'Authorization': f'Bearer {response.json()["access_token"]}'
    }


@pytest.fixture(scope='session')
def setup_browser():
    """Browser setup for OAuth flow"""
    browser.config.base_url = settings.OAUTH_URL
    browser.config.driver_name = settings.driver_name
    browser.config.timeout = settings.timeout
    browser.config.driver_options = webdriver.ChromeOptions()

    yield

    browser.quit()


@pytest.fixture(scope='session')
def user_auth_token(setup_browser):
    """
    Token for USER endpoints (favorites, playlists).
    Requires browser authorization (once per session).
    """
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')
    user_mail = os.getenv('user_email')
    user_password = os.getenv('user_password')
    callback_url = os.getenv('callback_url')

    # Authorization request
    auth_params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': callback_url,
        'scope': settings.permission_list
    }

    browser.open('/authorize?' + urlencode(auth_params))

    # Login flow
    browser.element('//input[@id="username"]').type(user_mail)
    browser.element('//button[@data-testid="login-button"]').click()

    # Click "Log in with password" if it appears
    try:
        browser.element('//button[contains(text(), "Log in with a password")]').click()
    except Exception:
        pass

    browser.element('//input[@id="password"]').type(user_password)
    browser.element('//button[@type="submit"]').click()
    time.sleep(5)

    # Accept permissions if prompt appears
    if browser.element("[data-testid='auth-accept']").matching(be.visible):
        browser.element("[data-testid='auth-accept']").perform(command.js.scroll_into_view).click()

    time.sleep(5)

    # Extract authorization code from callback URL
    current_url = browser.driver.current_url
    authorization_code = current_url.split('code=')[1].split('&')[0]

    # Exchange code for access token
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode('utf-8')

    token_response = requests.post(
        'https://accounts.spotify.com/api/token',
        headers={
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data={
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': callback_url
        }
    )

    assert token_response.status_code == 200, f"Token exchange failed: {token_response.text}"

    return {
        'Authorization': f'Bearer {token_response.json()["access_token"]}'
    }


@pytest.fixture(scope='session')
def user_id():
    return os.getenv('user_id')

@pytest.fixture(scope='session')
def search_client(client_credentials_token):
    """Search client for public endpoints"""
    return SearchClient(client_credentials_token)

@pytest.fixture(scope='session')
def track_client(client_credentials_token):
    """Track client for public endpoints"""
    return TrackClient(client_credentials_token)

@pytest.fixture(scope='session')
def user_track_client(user_auth_token):
    """Track client for user endpoints"""
    return TrackClient(user_auth_token)

@pytest.fixture(scope='session')
def playlist_client(user_auth_token):
    """Playlist client for user endpoints"""
    return PlaylistClient(user_auth_token)
