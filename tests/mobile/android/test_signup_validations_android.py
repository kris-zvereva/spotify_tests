import allure
from allure import step


@allure.feature("User Registration")
@allure.story("Sign up via Android app")
@allure.label("layer", "Mobile")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("signup", "android")
class TestSignUpValidationsAndroid:
    @allure.title("Email field is required for registration")
    @allure.description("Next button disabled and navigation blocked without email")
    def test_email_required_android(
        self, android_signup_page, test_user, assert_signup
    ):
        with step("Click signup button"):
            android_signup_page.click_signup_button()

        with step("Select continue with email option"):
            android_signup_page.click_continue_with_email()

        with step("Skip email and verify the next button is disabled"):
            android_signup_page.is_email_next_button_disabled()

            with step("Verify the hint is displayed"):
                assert_signup.verify_email_hint_displayed()

    @allure.title("Password field is required for registration")
    @allure.description("Next button disabled and navigation blocked without password")
    def test_password_required_android(
        self, android_signup_page, test_user, assert_signup
    ):
        with step("Click signup button"):
            android_signup_page.click_signup_button()

        with step("Select continue with email option"):
            android_signup_page.click_continue_with_email()

        with step("Fill email and click next"):
            android_signup_page.fill_signup_step_email(test_user["email"])

        with step("Skip password and and verify the next button is disabled"):
            android_signup_page.is_password_next_button_disabled()

            with step("Verify the hint is displayed"):
                assert_signup.verify_password_hint_displayed()

    @allure.title("Age validation prevents signup with default birth date")
    @allure.description(
        "Checks that the user is blocked from continuing signup "
        "when using the default birth date values."
    )
    def test_signup_is_blocked_with_default_birth_date(
        self, android_signup_page, test_user, assert_signup
    ):
        with step("Click signup button"):
            android_signup_page.click_signup_button()

        with step("Select continue with email option"):
            android_signup_page.click_continue_with_email()

        with step("Fill email and click next"):
            android_signup_page.fill_signup_step_email(test_user["email"])

        with step("Fill password and click next"):
            android_signup_page.fill_signup_step_password(test_user["password"])

        with step("Don't change the values in DOB and click next"):
            android_signup_page.click_age_next()

            with step("Verify age restriction error is displayed"):
                assert_signup.verify_dob_hint_displayed()
