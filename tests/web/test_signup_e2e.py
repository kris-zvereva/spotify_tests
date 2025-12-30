import allure
import pytest


@allure.feature("User Registration")
@allure.story("Sign up via web UI")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("layer", "UI")
@allure.tag("signup", "web", "smoke")
@pytest.mark.ci_skip
class TestSignUp:
    @allure.title("Successful user registration via web form")
    @allure.description(
        "Test verifies that a new user can successfully register through the Spotify signup form"
    )
    def test_signup_web(self, signup_page, test_user, assert_signup):
        signup_page.start_signup_email_flow()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(test_user["password"])
        signup_page.fill_signup_step_info(test_user)
        signup_page.fill_signup_step_terms()
        assert_signup.verify_successful_signup(test_user["username"])
