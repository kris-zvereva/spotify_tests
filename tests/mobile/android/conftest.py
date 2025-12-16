import pytest
import allure
import os
from appium import webdriver
from selene import browser

from model.assertions.android_signup_assertions import SignUpAssertionsAndroid
from model.pages.mobile.android.signup_page_android import SignUpPageAndroid
from data.user_data import generate_test_user
from utils.allure_attach import add_screenshot, attach_bstack_video
from mobile_config import mobile_settings, to_driver_options


@pytest.fixture(scope='function')
def android_driver():
    """Setup Android driver (local or remote)"""
    options = to_driver_options(mobile_settings)
    driver = webdriver.Remote(mobile_settings.remote_url, options=options)

    browser.config.driver = driver
    browser.config.timeout = mobile_settings.timeout

    yield driver

    # Allure attachments
    add_screenshot(browser)

    allure.attach(
        driver.page_source,
        name='Page source',
        attachment_type=allure.attachment_type.XML
    )

    # BrowserStack video (if remote)
    if mobile_settings.context == 'remote' and hasattr(driver, 'session_id'):
        bstack_username = mobile_settings.bstack_username
        bstack_access_key = mobile_settings.bstack_access_key

        if bstack_username and bstack_access_key:
            attach_bstack_video(
                driver.session_id,
                bstack_username,
                bstack_access_key
            )

    driver.quit()

@pytest.fixture
def android_signup_page(android_driver):
    """Returns Android SignUpPage instance"""
    return SignUpPageAndroid()

@pytest.fixture(scope='session')
def assert_signup():
    """Returns SignUpAssertionsAndroid instance"""
    return SignUpAssertionsAndroid()

@pytest.fixture
def test_user():
    """Generates random test user data"""
    return generate_test_user()