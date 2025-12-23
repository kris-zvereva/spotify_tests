from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser

from model.locators.android_signup_locators import SignUpPageLocatorsAndroid


class SignUpPageAndroid:
    """Android Spotify signup page"""

    def _hide_keyboard(self):
        """Hide keyboard if visible"""
        try:
            browser.driver.hide_keyboard()
        except Exception:
            pass

    def click_signup_button(self):
        browser.element(SignUpPageLocatorsAndroid.SIGNUP_BUTTON).click()

    def click_continue_with_email(self):
        browser.element(SignUpPageLocatorsAndroid.CONTINUE_WITH_EMAIL).click()

    def fill_email(self, email):
        browser.element(SignUpPageLocatorsAndroid.EMAIL_INPUT).type(email)
        self._hide_keyboard()

    def click_email_next(self):
        browser.element(SignUpPageLocatorsAndroid.EMAIL_NEXT_BUTTON).click()

    def is_email_next_button_disabled(self):
        browser.element(SignUpPageLocatorsAndroid.EMAIL_NEXT_BUTTON).should(be.disabled)

    def fill_signup_step_email(self, email):
        self.fill_email(email)
        self.click_email_next()

    def fill_password(self, password):
        browser.element(SignUpPageLocatorsAndroid.PASSWORD_INPUT).type(password)
        self._hide_keyboard()

    def click_password_next(self):
        browser.element(SignUpPageLocatorsAndroid.PASSWORD_NEXT_BUTTON).click()

    def is_password_next_button_disabled(self):
        browser.element(SignUpPageLocatorsAndroid.PASSWORD_NEXT_BUTTON).should(
            be.disabled
        )

    def fill_signup_step_password(self, password):
        self.fill_password(password)
        self.click_password_next()

    def click_age_next(self):
        browser.element(SignUpPageLocatorsAndroid.AGE_NEXT_BUTTON).click()

    def fill_signup_step_birthday(self, birthday_dict):
        self._fill_birthday_year(birthday_dict)
        self.click_age_next()

    def select_gender(self, gender):
        locator = SignUpPageLocatorsAndroid.GENDER_LOCATORS[gender]
        browser.element(locator).click()

    def fill_username(self, username):
        browser.element(SignUpPageLocatorsAndroid.USERNAME_INPUT).type(username)
        self._hide_keyboard()

    def agree_to_terms(self):
        browser.element(SignUpPageLocatorsAndroid.AGREE_TERMS_SWITCH).click()

    def agree_to_marketing(self):
        browser.element(SignUpPageLocatorsAndroid.AGREE_MARKETING_SWITCH).click()

    def click_create_account(self):
        browser.element(SignUpPageLocatorsAndroid.CREATE_ACCOUNT_BUTTON).click()

    def decline_notifications(self):
        browser.element(SignUpPageLocatorsAndroid.DECLINE_NOTIFICATION_BUTTON).click()

    def search_and_select_artist(self, artist_names):
        for artist in artist_names:
            browser.element(SignUpPageLocatorsAndroid.SEARCH_FIELD).click()
            browser.element(SignUpPageLocatorsAndroid.SEARCH_INPUT).type(artist)
            self._hide_keyboard()
            browser.element(SignUpPageLocatorsAndroid.FIRST_SUGGESTED_ARTIST).click()

    def click_done(self):
        browser.element(SignUpPageLocatorsAndroid.DONE_BUTTON).click()
        return self

    def click_not_now(self):
        browser.element(SignUpPageLocatorsAndroid.NOT_NOW_BUTTON).click()

    def _fill_birthday_year(self, birthday_dict, max_attempts: int = 10):
        driver = browser.driver
        target_year = str(birthday_dict["year"])

        picker_locator = SignUpPageLocatorsAndroid.BIRTH_YEAR_PICKER
        scroll_selector = SignUpPageLocatorsAndroid.YEAR_PICKER_SCROLL

        for attempt in range(max_attempts):
            current_year = driver.find_element(*picker_locator).get_attribute("text")
            if current_year == target_year:
                return

            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_selector)
