class SignUpPageLocators:
    SIGNUP_BUTTON = '//button[@data-testid="signup-button"]'
    SUBMIT_BUTTON = '//button[@data-testid="submit"]'

    EMAIL_INPUT = '//input[@id="username"]'
    PASSWORD_INPUT = '//input[@name="new-password"]'
    USERNAME_INPUT = '//input[@name="displayName"]'
    BD_DATE_INPUT = '//input[@data-testid="birthDateDay"]'
    BD_MONTH_INPUT = '//select[@data-testid="birthDateMonth"]'
    BD_YEAR_INPUT = '//input[@data-testid="birthDateYear"]'

    GENDER_LOCATOR_TEMPLATE = '//label[@for="gender_option_{gender}"]'

    MARKETING_CHECKBOX = '//label[@for="checkbox-marketing"]'
    PRIVACY_CHECKBOX = '//label[@for="checkbox-privacy"]'
    USER_ACCOUNT_BUTTON = '//button[@data-testid="user-widget-link"]'


class SignUpErrorLocators:
    """Locators for signup error messages"""

    EMAIL_ERROR_MESSAGE = '//div[@id="username-error-message"]//span'

    PASSWORD_REQUIREMENT_TEMPLATE = '//li[@id="password_requirement_{requirement}"]//span[contains(text(), "{status}")]'

    USERNAME_ERROR_MESSAGE = '//div[@id="displayname-error-message"]//span'
    GENDER_ERROR_MESSAGE = '//div[@id="gender-error-message"]//span'

    BIRTHDAY_ERROR_MESSAGE = '//div[@id="birthdate-error-invalid"]//span'
    BIRTHDAY_DAY_ERROR_MESSAGE = '//div[@id="birthdate-error-day_invalid"]//span'
    BIRTHDAY_MONTH_ERROR_MESSAGE = '//div[@id="birthdate-error-month_invalid"]//span'
    BIRTHDAY_YEAR_ERROR_MESSAGE = (
        '(//div[@id="birthdate-error-year_below_1900"]//span)[2]'
    )
