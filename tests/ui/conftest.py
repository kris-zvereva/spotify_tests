import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from model.assertions.web_signup_assertions import SignUpAssertions
from model.pages.web.web_signup_page import SignUpPage
from utils.user_data import generate_test_user


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    # disables anti-bot protection
    options.add_argument('--disable-blink-features=AutomationControlled')

    # english locale
    options.add_argument('--lang=en-US')
    options.add_experimental_option('prefs', {
        'intl.accept_languages': 'en-US,en'
    })

    driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 10

    yield browser

    browser.quit()
    # TODO attach allure

@pytest.fixture
def signup_page():
    """Returns SignUpPage instance"""
    return SignUpPage()

@pytest.fixture(scope='session')
def assert_signup():
    return SignUpAssertions()


@pytest.fixture
def test_user():
    """Generates random test user data"""
    return generate_test_user()