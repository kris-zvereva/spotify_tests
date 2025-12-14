class SignUpPageLocators:
    SIGNUP_URL = "https://open.spotify.com/"  # TODO вынести куда-нибудь
    SIGNUP_BUTTON = '//button[@data-testid="signup-button"]'
    SUBMIT_BUTTON = '//button[@data-testid="submit"]'

    EMAIL_INPUT = '//input[@id="username"]'
    PASSWORD_INPUT = '//input[@name="new-password"]'
    USERNAME_INPUT = '//input[@name="displayName"]'
    BD_DATE_INPUT = '//input[@data-testid="birthDateDay"]'
    BD_MONTH_INPUT = '//select[@data-testid="birthDateMonth"]'
    BD_YEAR_INPUT = '//input[@data-testid="birthDateYear"]'

    GENDER_LOCATORS = {
        "male": '//label[@for="gender_option_male"]',
        "female": '//label[@for="gender_option_female"]',
        "non_binary": '//label[@for="gender_option_non_binary"]',
        "other": '//label[@for="gender_option_other"]',
        "prefer_not_to_say": '//label[@for="gender_option_prefer_not_to_say"]'
    }
    MARKETING_CHECKBOX = '//label[@for="checkbox-marketing"]'
    PRIVACY_CHECKBOX = '//label[@for="checkbox-privacy"]'
    USER_ACCOUNT_BUTTON = '//button[@data-testid="user-widget-link"]'

class SignUpErrorLocators:
    """Locators for signup error messages"""

    EMAIL_ERROR_MESSAGE = '//div[@id="username-error-message"]//span'

    PASSWORD_TEN_CHARS_NOT_MET = '//li[@id="password_requirement_ten_characters"]//span[contains(text(), "Not met")]'
    PASSWORD_TEN_CHARS_MET = '//li[@id="password_requirement_ten_characters"]//span[contains(text(), "Met")]'

    PASSWORD_LETTER_NOT_MET = '//li[@id="password_requirement_one_letter"]//span[contains(text(), "Not met")]'
    PASSWORD_LETTER_MET = '//li[@id="password_requirement_one_letter"]//span[contains(text(), "Met")]'

    PASSWORD_NUMBER_SPECIAL_NOT_MET = '//li[@id="password_requirement_one_number_or_special_character"]//span[contains(text(), "Not met")]'
    PASSWORD_NUMBER_SPECIAL_MET = '//li[@id="password_requirement_one_number_or_special_character"]//span[contains(text(), "Met")]'

    USERNAME_ERROR_MESSAGE = '//div[@id="displayname-error-message"]//span'
    GENDER_ERROR_MESSAGE = '//div[@id="gender-error-message"]//span'

    BIRTHDAY_ERROR_MESSAGE = '//div[@id="birthdate-error-invalid"]//span'
    BIRTHDAY_DAY_ERROR_MESSAGE = '//div[@id="birthdate-error-day_invalid"]//span'
    BIRTHDAY_MONTH_ERROR_MESSAGE = '//div[@id="birthdate-error-month_invalid"]//span'
    BIRTHDAY_YEAR_ERROR_MESSAGE = '//div[@id="birthdate-error-year_invalid"]//span'
