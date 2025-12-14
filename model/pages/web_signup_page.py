import time

from selene import browser, by, be

from model.locators.web_signup_page_locators import SignUpPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class SignUpPage:

    def _click_with_human_simulation(self, locator):
        """disables anti-bot protection"""
        element = browser.element(by.xpath(locator))

        browser.driver.execute_script("arguments[0].scrollIntoView(true);", element())
        time.sleep(0.2)

        actions = ActionChains(browser.driver)
        actions.move_to_element(element())
        actions.pause(0.4)
        actions.click()
        actions.perform()

    def _fill_email_input(self, user_email):
        browser.element(by.xpath(SignUpPageLocators.EMAIL_INPUT)).type(user_email)

    def _fill_password_input(self, user_password):
        browser.element(by.xpath(SignUpPageLocators.PASSWORD_INPUT)).type(user_password)

    def _fill_username(self, username):
        browser.element(by.xpath(SignUpPageLocators.USERNAME_INPUT)).type(username)

    def _fill_birthday(self, user_bd):
        browser.element(by.xpath(SignUpPageLocators.BD_DATE_INPUT)).type(user_bd['day'])
        browser.element(by.xpath(SignUpPageLocators.BD_MONTH_INPUT)).type(user_bd['month'])
        browser.element(by.xpath(SignUpPageLocators.BD_YEAR_INPUT)).type(user_bd['year'])

    def _fill_gender(self, user_gender):
        locator = SignUpPageLocators.GENDER_LOCATORS[user_gender]
        self._click_with_human_simulation(locator)

    def open_signup_page(self):
        browser.open(SignUpPageLocators.SIGNUP_URL)
        browser.element(by.xpath(SignUpPageLocators.SIGNUP_BUTTON)).should(be.visible)

    def click_submit_button(self):
        self._click_with_human_simulation(SignUpPageLocators.SUBMIT_BUTTON)

    def click_signup_button(self):
        self._click_with_human_simulation(SignUpPageLocators.SIGNUP_BUTTON)
        browser.element(by.xpath(SignUpPageLocators.EMAIL_INPUT)).should(be.visible)

    def fill_signup_step_email(self, user_email):
        self._fill_email_input(user_email)
        self.click_submit_button()

    def fill_signup_step_password(self, user_password):
        self._fill_password_input(user_password)
        self.click_submit_button()

    def fill_signup_step_info(self, user_data):
        self._fill_username(user_data['username'])
        self._fill_birthday(user_data['birthday'])
        self._fill_gender(user_data['gender'])
        self.click_submit_button()

    def fill_signup_step_terms(self):
        browser.element(by.xpath(SignUpPageLocators.MARKETING_CHECKBOX)).click()
        browser.element(by.xpath(SignUpPageLocators.PRIVACY_CHECKBOX)).click()
        self.click_submit_button()

    def fill_partial_birthday(self, day=None, month=None, year=None):
        """
        Fill birthday fields partially for validation testing
        Args:
            day: Day value (optional)
            month: Month value (optional)
            year: Year value (optional)
        """
        if day:
            browser.element(by.xpath(SignUpPageLocators.BD_DATE_INPUT)).type(day)
        if month:
            browser.element(by.xpath(SignUpPageLocators.BD_MONTH_INPUT)).type(month)
        if year:
            browser.element(by.xpath(SignUpPageLocators.BD_YEAR_INPUT)).type(year)
        self.click_submit_button()
