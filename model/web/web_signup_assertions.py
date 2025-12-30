import allure
from selene import be, browser, by, have

from model.common.enums import PasswordRequirement, PasswordRequirementStatus
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

    def assert_password_requirement(
        self, requirement: PasswordRequirement, status: PasswordRequirementStatus
    ):
        locator = SignUpErrorLocators.PASSWORD_REQUIREMENT_TEMPLATE.format(
            requirement=requirement.value, status=status.value
        )
        browser.element(locator).should(be.present)

    @allure.step("Verify password validation rules display")
    def verify_password_validation_state(
        self, ten_chars_met: bool, letter_met: bool, number_special_met: bool
    ):
        self.assert_password_requirement(
            PasswordRequirement.TEN_CHARACTERS,
            PasswordRequirementStatus.MET
            if ten_chars_met
            else PasswordRequirementStatus.NOT_MET,
        )
        self.assert_password_requirement(
            PasswordRequirement.ONE_LETTER,
            PasswordRequirementStatus.MET
            if letter_met
            else PasswordRequirementStatus.NOT_MET,
        )
        self.assert_password_requirement(
            PasswordRequirement.NUMBER_OR_SPECIAL,
            PasswordRequirementStatus.MET
            if number_special_met
            else PasswordRequirementStatus.NOT_MET,
        )

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
