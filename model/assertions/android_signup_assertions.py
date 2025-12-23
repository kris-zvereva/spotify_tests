from selene import be, browser, have

from model.enums.signup_error_messages import ErrorMessages
from model.locators.android_signup_locators import (
    SignUpErrorLocatorsAndroid,
    SignUpPageLocatorsAndroid,
)


class SignUpAssertionsAndroid:
    """All signup verification methods for android"""

    def verify_profile_button_visible(self):
        """Verify profile settings button is visible"""
        browser.element(SignUpPageLocatorsAndroid.GO_TO_PROFILE_SETTINGS).should(
            be.visible
        )

    def verify_email_hint_displayed(self):
        """Verify email hint is visible"""
        browser.element(SignUpErrorLocatorsAndroid.EMAIL_ERROR_MESSAGE).should(
            be.visible
        )
        browser.element(SignUpErrorLocatorsAndroid.EMAIL_ERROR_MESSAGE).should(
            have.text(ErrorMessages.EMAIL_HINT.value)
        )

    def verify_password_hint_displayed(self):
        """Verify password hint is visible"""
        browser.element(SignUpErrorLocatorsAndroid.PASSWORD_ERROR_MESSAGE).should(
            be.visible
        )
        browser.element(SignUpErrorLocatorsAndroid.PASSWORD_ERROR_MESSAGE).should(
            have.text(ErrorMessages.PASSWORD_HINT.value)
        )

    def verify_dob_hint_displayed(self):
        """Verify DOB hint is visible"""
        browser.element(SignUpErrorLocatorsAndroid.DOB_ERROR_MESSAGE).should(be.visible)
        browser.element(SignUpErrorLocatorsAndroid.DOB_ERROR_MESSAGE).should(
            have.text(ErrorMessages.DOB_HINT.value)
        )
