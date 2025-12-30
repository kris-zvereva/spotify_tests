import allure
from selene import be, browser, have

from model.enums.signup_error_messages import ErrorMessages
from model.mobile.android_signup_locators import (
    SignUpErrorLocatorsAndroid,
    SignUpPageLocatorsAndroid,
)


class SignUpAssertionsAndroid:
    """All signup verification methods for android"""

    @allure.step("Verify the account button is displayed")
    def verify_profile_button_visible(self):
        """Verify profile settings button is visible"""
        browser.element(SignUpPageLocatorsAndroid.GO_TO_PROFILE_SETTINGS).should(
            be.visible
        )

    @allure.step("Verify the email hint is displayed")
    def verify_email_hint_displayed(self):
        """Verify email hint is visible"""
        browser.element(SignUpErrorLocatorsAndroid.EMAIL_ERROR_MESSAGE).should(
            be.visible
        )
        browser.element(SignUpErrorLocatorsAndroid.EMAIL_ERROR_MESSAGE).should(
            have.text(ErrorMessages.EMAIL_HINT.value)
        )

    @allure.step("Verify the password hint is displayed")
    def verify_password_hint_displayed(self):
        """Verify password hint is visible"""
        browser.element(SignUpErrorLocatorsAndroid.PASSWORD_ERROR_MESSAGE).should(
            be.visible
        )
        browser.element(SignUpErrorLocatorsAndroid.PASSWORD_ERROR_MESSAGE).should(
            have.text(ErrorMessages.PASSWORD_HINT.value)
        )

    @allure.step("Verify the DOB hint is displayed")
    def verify_dob_hint_displayed(self):
        """Verify DOB hint is visible"""
        browser.element(SignUpErrorLocatorsAndroid.DOB_ERROR_MESSAGE).should(be.visible)
        browser.element(SignUpErrorLocatorsAndroid.DOB_ERROR_MESSAGE).should(
            have.text(ErrorMessages.DOB_HINT.value)
        )
