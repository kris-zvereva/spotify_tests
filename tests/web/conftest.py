import os

import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import settings
from data.user_data import generate_test_user
from model.assertions.web_signup_assertions import SignUpAssertions
from model.pages.web.web_signup_page import SignUpPage
from utils.allure_attach import add_screenshot, attach_browser_logs, attach_bstack_video

load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = Options()
    # disables anti-bot protection
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-gpu")

    # english locale
    options.add_argument("--lang=en-US")
    options.add_experimental_option("prefs", {"intl.accept_languages": "en-US,en"})

    context = os.getenv("WEB_CONTEXT", "remote")

    if context == "remote":
        options.set_capability(
            "bstack:options",
            {
                "projectName": "Spotify_Web_Tests",
                "buildName": "Web_Signup_Tests",
                "userName": os.getenv("browserstack_username"),
                "accessKey": os.getenv("browserstack_access_key"),
            },
        )

        driver = webdriver.Remote(
            command_executor=settings.BROWSERSTACK_URL, options=options
        )
    else:
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield browser

    add_screenshot(browser)
    attach_browser_logs(browser.driver)

    allure.attach(
        browser.driver.page_source,
        name="Page source",
        attachment_type=allure.attachment_type.HTML,
    )

    if hasattr(browser.driver, "session_id"):
        bstack_username = os.getenv("browserstack_username")
        bstack_access_key = os.getenv("browserstack_access_key")

        if bstack_username and bstack_access_key:
            attach_bstack_video(
                browser.driver.session_id, bstack_username, bstack_access_key
            )

    browser.quit()


@pytest.fixture
def signup_page():
    return SignUpPage()


@pytest.fixture(scope="session")
def assert_signup():
    return SignUpAssertions()


@pytest.fixture
def test_user():
    """Generates random test user data"""
    return generate_test_user()
