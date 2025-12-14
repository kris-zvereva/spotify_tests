from enum import Enum


class ErrorMessages(Enum):
    EMPTY_EMAIL_ERROR = "This email is invalid. Make sure it's written like example@email.com"
    EMPTY_USERNAME_ERROR = "Enter a name for your profile."
    EMPTY_BIRTHDAY_ERROR = "Please enter your date of birth."
    EMPTY_GENDER_ERROR = "Select your gender."
    BD_INVALID_DAY_RANGE_ERROR = "Please enter the day of your birth date by entering a number between 1 and 31."
    BD_MONTH_REQUIRED_ERROR = "Select your birth month."
    BD_INVALID_YEAR_FORMAT_ERROR = "Please enter the year of your birth date using four digits (e.g., 1990)."