import os

import allure
import pytest
from allure import step


@allure.feature("User Registration")
@allure.story("Sign up via Android app")
@allure.label("layer", "Mobile")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("signup", "android", "smoke")
@pytest.mark.skipif(
    os.getenv("MOBILE_CONTEXT") == "remote",
    reason="Flaky due to Spotify's anti-bot protection (reCAPTCHA). Passes locally but fails in headless CI environment",
)
class TestSignUpAndroid:
    @allure.title("Successful user registration via Android app")
    @allure.description(
        "Verifies user can successfully register through Spotify Android signup flow"
    )
    def test_signup_android(self, android_signup_page, test_user, assert_signup):
        with step("Click signup button"):
            android_signup_page.click_signup_button()

        with step("Select continue with email option"):
            android_signup_page.click_continue_with_email()

        with step("Fill email and click next"):
            android_signup_page.fill_signup_step_email(test_user["email"])

        with step("Fill password and click next"):
            android_signup_page.fill_signup_step_password(test_user["password"])

        with step("Select DOB and click next"):
            android_signup_page.fill_signup_step_birthday(test_user["birthday"])

        with step("Select gender"):
            android_signup_page.select_gender(test_user["gender"])

        with step("Fill username"):
            android_signup_page.fill_username(test_user["username"])

        with step("Agree to the terms"):
            android_signup_page.agree_to_terms()
            android_signup_page.agree_to_marketing()

        with step("click Create account button"):
            android_signup_page.click_create_account()

        with step("Skip notifications"):
            android_signup_page.decline_notifications()

        with step("Find and select the artists"):
            android_signup_page.search_and_select_artist(test_user["artists"])

        with step("Click Done button"):
            android_signup_page.click_done()

        with step("Skip listening by clicking not now button"):
            android_signup_page.click_not_now()

        with step("Verify the account button is displayed"):
            assert_signup.verify_profile_button_visible()
