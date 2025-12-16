import allure
from allure import step


@allure.feature('User Registration')
@allure.story('Sign up via web UI')
@allure.severity(allure.severity_level.CRITICAL)
@allure.label('layer', 'UI')
@allure.tag('signup', 'web', 'smoke')
class TestSignUp:

    @allure.title('Successful user registration via web form')
    @allure.description('Test verifies that a new user can successfully register through the Spotify signup form')
    def test_signup_web(self, signup_page, test_user, assert_signup):
        with step('Open signup page'):
            signup_page.open_signup_page()

        with step('Click signup button'):
            signup_page.click_signup_button()

        with step('Fill email'):
            signup_page.fill_signup_step_email(test_user['email'])

        with step('Fill password'):
            signup_page.fill_signup_step_password(test_user['password'])

        with step('Fill user info: username, gender and DOB'):
            signup_page.fill_signup_step_info(test_user)

        with step('Accept terms and conditions'):
            signup_page.fill_signup_step_terms()

            with step(f'Verify successful signup for user: {test_user["username"]}'):
                assert_signup.verify_successful_signup(test_user['username'])
