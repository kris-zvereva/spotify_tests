import allure

from data.user_data import INVALID_BIRTHDAYS, INVALID_PASSWORDS


@allure.feature("User Registration")
@allure.story("Form validation")
@allure.label("layer", "UI")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("signup", "web")
class TestSignUpValidation:
    @allure.title("Email field is required")
    @allure.description("Verifies email validation error when field is skipped")
    def test_email_is_required(self, signup_page, test_user, assert_signup):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.click_submit_button()
        assert_signup.verify_email_error()

    @allure.title("Password must contain at least 10 characters")
    @allure.description(
        "Verifies password length validation rule when password is less than 10 characters"
    )
    def test_password_min_10_chars(self, signup_page, test_user, assert_signup):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(INVALID_PASSWORDS["too_short"])
        assert_signup.verify_password_validation_state(
            ten_chars_met=False, letter_met=True, number_special_met=True
        )

    @allure.title("Password must contain at least one letter")
    @allure.description(
        "Verifies letter requirement validation when password has no letters"
    )
    def test_password_must_have_letter(self, signup_page, test_user, assert_signup):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(INVALID_PASSWORDS["no_letter"])
        assert_signup.verify_password_validation_state(
            ten_chars_met=True, letter_met=False, number_special_met=True
        )

    @allure.title("Password must contain at least one number or special character")
    @allure.description(
        "Verifies number/special requirement validation when password has only letters"
    )
    def test_password_must_have_number_or_special(
        self, signup_page, test_user, assert_signup
    ):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(INVALID_PASSWORDS["no_number_or_special"])
        assert_signup.verify_password_validation_state(
            ten_chars_met=True, letter_met=True, number_special_met=False
        )

    @allure.title("Personal info fields are required")
    @allure.description(
        "Verifies validation errors for empty username, birthday and gender fields"
    )
    def test_step_personal_info_required_fields(
        self, signup_page, test_user, assert_signup
    ):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(test_user["password"])
        signup_page.click_submit_button()
        assert_signup.verify_username_error()
        assert_signup.verify_birthday_error()
        assert_signup.verify_gender_error()

    @allure.title("Birthday day must be between 1 and 31")
    @allure.description(
        "Verifies day validation error when value is outside valid range"
    )
    def test_birthday_day_error(self, signup_page, test_user, assert_signup):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(test_user["password"])
        signup_page.fill_partial_birthday(INVALID_BIRTHDAYS["invalid_day"])
        assert_signup.verify_birthday_day_error()

    @allure.title("Birthday month is required")
    @allure.description("Verifies month validation error when field is empty")
    def test_birthday_empty_month(self, signup_page, test_user, assert_signup):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(test_user["password"])
        signup_page.fill_partial_birthday(INVALID_BIRTHDAYS["missing_month"])
        assert_signup.verify_birthday_month_error()

    @allure.title("Birthday year must be 4 digits")
    @allure.description("Verifies error when year is not entered using 4 digits")
    def test_birthday_invalid_year(self, signup_page, test_user, assert_signup):
        signup_page.open_signup_page()
        signup_page.click_signup_button()
        signup_page.fill_signup_step_email(test_user["email"])
        signup_page.fill_signup_step_password(test_user["password"])
        signup_page.fill_partial_birthday(INVALID_BIRTHDAYS["invalid_year"])
        assert_signup.verify_birthday_year_error()
