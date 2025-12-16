from selene import browser, be

from model.locators.android_signup_locators import SignUpPageLocatorsAndroid, SignUpErrorLocatorsAndroid


class SignUpAssertionsAndroid:
    """All signup verification methods for android"""

    def verify_profile_button_visible(self):
        """Verify profile settings button is visible"""
        browser.element(SignUpPageLocatorsAndroid.GO_TO_PROFILE_SETTINGS).should(be.visible)

    def verify_email_error_displayed(self):
        """Verify email error is visible"""
        browser.element(SignUpErrorLocatorsAndroid.EMAIL_ERROR_MESSAGE).should(be.visible)

    def verify_password_error_displayed(self):
        """Verify password error is visible"""
        browser.element(SignUpErrorLocatorsAndroid.PASSWORD_ERROR_MESSAGE).should(be.visible)
