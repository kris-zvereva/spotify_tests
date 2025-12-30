import allure
from selene import be, browser, by, have

from model.enums.signup_error_messages import ErrorMessages
from model.web.web_signup_page_locators import (
    SignUpErrorLocators,
    SignUpPageLocators,
)


class SignUpAssertions:
    """All signup verification methods for web"""

    @allure.step("Verify successful signup for user")
    def verify_successful_signup(self, username):
        browser.element(by.xpath(SignUpPageLocators.USER_ACCOUNT_BUTTON)).should(
            have.attribute("aria-label").value(username)
        )

    @allure.step("Verify the error message is displayed")
    def verify_email_error(self):
        browser.element(by.xpath(SignUpErrorLocators.EMAIL_ERROR_MESSAGE)).should(
            have.text(ErrorMessages.EMPTY_EMAIL_ERROR.value)
        )

    @allure.step("Verify the error message for empty username is displayed")
    def verify_username_error(self):
        browser.element(by.xpath(SignUpErrorLocators.USERNAME_ERROR_MESSAGE)).should(
            have.text(ErrorMessages.EMPTY_USERNAME_ERROR.value)
        )

    @allure.step("Verify the error message for empty birthday is displayed")
    def verify_birthday_error(self):
        browser.element(by.xpath(SignUpErrorLocators.BIRTHDAY_ERROR_MESSAGE)).should(
            have.text(ErrorMessages.EMPTY_BIRTHDAY_ERROR.value)
        )

    @allure.step("Verify the error message for empty gender is displayed")
    def verify_gender_error(self):
        browser.element(by.xpath(SignUpErrorLocators.GENDER_ERROR_MESSAGE)).should(
            have.text(ErrorMessages.EMPTY_GENDER_ERROR.value)
        )

    @allure.step("Verify password validation rules display")
    def verify_password_validation_state(
        self, ten_chars_met, letter_met, number_special_met
    ):
        """
        Verify password validation rules display
        Args:
            ten_chars_met: True if 10 chars requirement met
            letter_met: True if letter requirement met
            number_special_met: True if number/special requirement met
        """
        if ten_chars_met:
            browser.element(
                by.xpath(SignUpErrorLocators.PASSWORD_TEN_CHARS_MET)
            ).should(be.present)
        else:
            browser.element(
                by.xpath(SignUpErrorLocators.PASSWORD_TEN_CHARS_NOT_MET)
            ).should(be.present)

        if letter_met:
            browser.element(by.xpath(SignUpErrorLocators.PASSWORD_LETTER_MET)).should(
                be.present
            )
        else:
            browser.element(
                by.xpath(SignUpErrorLocators.PASSWORD_LETTER_NOT_MET)
            ).should(be.present)

        if number_special_met:
            browser.element(
                by.xpath(SignUpErrorLocators.PASSWORD_NUMBER_SPECIAL_MET)
            ).should(be.present)
        else:
            browser.element(
                by.xpath(SignUpErrorLocators.PASSWORD_NUMBER_SPECIAL_NOT_MET)
            ).should(be.present)

    @allure.step("Verify the error message for birthday day is displayed")
    def verify_birthday_day_error(self):
        browser.element(
            by.xpath(SignUpErrorLocators.BIRTHDAY_DAY_ERROR_MESSAGE)
        ).should(have.text(ErrorMessages.BD_INVALID_DAY_RANGE_ERROR.value))

    @allure.step("Verify the error message for birthday month is displayed")
    def verify_birthday_month_error(self):
        browser.element(
            by.xpath(SignUpErrorLocators.BIRTHDAY_MONTH_ERROR_MESSAGE)
        ).should(have.text(ErrorMessages.BD_MONTH_REQUIRED_ERROR.value))

    @allure.step("Verify the error message for birthday year is displayed")
    def verify_birthday_year_error(self):
        browser.element(
            by.xpath(SignUpErrorLocators.BIRTHDAY_YEAR_ERROR_MESSAGE)
        ).should(have.text(ErrorMessages.BD_INVALID_YEAR_FORMAT_ERROR.value))
