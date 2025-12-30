import allure
import pytest


@allure.feature("User Registration")
@allure.story("Sign up via Android app")
@allure.label("layer", "Mobile")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("signup", "android", "smoke")
@pytest.mark.ci_skip
class TestSignUpAndroid:
    @allure.title("Successful user registration via Android app")
    @allure.description(
        "Verifies user can successfully register through Spotify Android signup flow"
    )
    def test_signup_android(self, android_signup_page, test_user, assert_signup):
        android_signup_page.click_signup_button()
        android_signup_page.click_continue_with_email()
        android_signup_page.fill_signup_step_email(test_user["email"])
        android_signup_page.fill_signup_step_password(test_user["password"])
        android_signup_page.fill_signup_step_birthday(test_user["birthday"])
        android_signup_page.select_gender(test_user["gender"])
        android_signup_page.fill_username(test_user["username"])
        android_signup_page.agree_to_terms()
        android_signup_page.agree_to_marketing()
        android_signup_page.click_create_account()
        android_signup_page.decline_notifications()
        android_signup_page.search_and_select_artist(test_user["artists"])
        android_signup_page.click_done()
        android_signup_page.click_not_now()
        assert_signup.verify_profile_button_visible()
