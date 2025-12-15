from selene import browser, be

from model.locators.android_signup_locators import SignUpPageLocatorsAndroid


class SignUpAssertionsAndroid:
    """All signup verification methods for android"""

    def verify_profile_button_visible(self):
        """Verify profile settings button is visible (Android)"""
        browser.element(SignUpPageLocatorsAndroid.GO_TO_PROFILE_SETTINGS).should(be.visible)
