import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser

from model.assertions.android_signup_assertions import SignUpAssertionsAndroid
from model.pages.mobile.android.signup_page_android import SignUpPageAndroid
from utils.user_data import generate_test_user


@pytest.fixture(scope='function')
def android_driver():
    """Setup Android driver"""
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.device_name = 'emulator-5554'
    options.app = '/Users/kristinazvereva/PycharmProjects/spotify_tests/apps/spotify.apk'
    options.app_package = 'com.spotify.music'
    options.app_activity = '.MainActivity'
    options.no_reset = True

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)


    browser.config.driver = driver
    browser.config.timeout = 20

    # Ждём запуска приложения
    #time.sleep(3)  # Даём время приложению запуститься

    yield driver

    driver.quit()
    # todo allure attach screenshots if failed


@pytest.fixture
def android_signup_page(android_driver):
    """Returns Android SignUpPage instance"""
    return SignUpPageAndroid()

@pytest.fixture(scope='session')
def assert_signup():
    return SignUpAssertionsAndroid()

@pytest.fixture
def test_user():
    """Generates random test user data"""
    return generate_test_user()