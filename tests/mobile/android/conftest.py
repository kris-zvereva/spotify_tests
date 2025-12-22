import sys
from pathlib import Path
import os
import pytest
import allure
from appium import webdriver
from selene import browser

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from model.assertions.android_signup_assertions import SignUpAssertionsAndroid
from model.pages.mobile.android.signup_page_android import SignUpPageAndroid
from data.user_data import generate_test_user
from utils.allure_attach import add_screenshot, attach_bstack_video
from mobile_config import mobile_settings, to_driver_options


@pytest.fixture(scope='function')
def android_driver():
    """Setup Android driver (local or remote)"""
    options = to_driver_options(mobile_settings)

    context = os.getenv('MOBILE_CONTEXT', 'local')
    if context == 'remote':
        username = os.getenv('browserstack_username')
        accesskey = os.getenv('browserstack_access_key')
        remote_url = f"https://{username}:{accesskey}@hub-cloud.browserstack.com/wd/hub"
    else:
        remote_url = mobile_settings.remote_url  # http://127.0.0.1:4723

    driver = webdriver.Remote(remote_url, options=options)

    browser.config.driver = driver
    browser.config.timeout = mobile_settings.timeout

    yield driver

    # Allure attachments (spotify doesnt allow screenshots in some signup forms)
    try:
        add_screenshot(browser)
    except Exception as e:
        print(f"Screenshot failed: {e}")

    allure.attach(
        driver.page_source,
        name='Page source',
        attachment_type=allure.attachment_type.XML
    )

    # BrowserStack video
    context = os.getenv('MOBILE_CONTEXT', 'local')
    if context == 'remote':
        attach_bstack_video(
            driver.session_id,
            os.getenv('browserstack_username'),
            os.getenv('browserstack_access_key'),
            is_mobile=True,
        )


    driver.execute_script('mobile: clearApp', {'appId': 'com.spotify.music'})
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