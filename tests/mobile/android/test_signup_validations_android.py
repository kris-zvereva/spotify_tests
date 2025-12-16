import allure
from allure import step

@allure.feature('User Registration')
@allure.story('Sign up via Android app')
@allure.label('layer', 'Mobile')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag('signup', 'android', 'smoke')
class TestSignUpValidationsAndroid:

    @allure.title('Email field is required for registration')
    @allure.description('Next button disabled and navigation blocked without email')
    def test_email_required_android(self, android_signup_page, test_user, assert_signup):
        with step('Click signup button'):
            android_signup_page.click_signup_button()

        with step('Select continue with email option'):
            android_signup_page.click_continue_with_email()

        with step('Skip email and verify the next button is disabled'):
            android_signup_page.is_email_next_button_disabled()

            with step('Verify the error is displayed'):
                assert_signup.verify_email_error_displayed()


    @allure.title('Password field is required for registration')
    @allure.description('Next button disabled and navigation blocked without password')
    def test_password_required_android(self, android_signup_page, test_user, assert_signup):
        with step('Click signup button'):
            android_signup_page.click_signup_button()

        with step('Select continue with email option'):
            android_signup_page.click_continue_with_email()

        with step('Fill email and click next'):
            android_signup_page.fill_signup_step_email(test_user['email'])

        with step('Skip password and and verify the next button is disabled'):
            android_signup_page.is_password_next_button_disabled()

            with step('Verify the error is displayed'):
                assert_signup.verify_password_error_displayed()