from appium.webdriver.common.appiumby import AppiumBy


class SignUpPageLocatorsAndroid:
    SIGNUP_URL = "https://open.spotify.com/"  # TODO вынести куда-нибудь
    SIGNUP_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up free")')
    CONTINUE_WITH_EMAIL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue with email")')

    EMAIL_INPUT = (AppiumBy.ID, 'com.spotify.music:id/email')
    EMAIL_NEXT_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/email_next_button')

    PASSWORD_INPUT = (AppiumBy.ID, 'com.spotify.music:id/input_password')
    PASSWORD_NEXT_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/password_next_button')

    # TODO doublechek
    BIRTH_MONTH_PICKER = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("android:id/numberpicker_input").instance(0)'
)

    BIRTH_DAY_PICKER = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("android:id/numberpicker_input").instance(1)'
    )

    BIRTH_YEAR_PICKER = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("android:id/numberpicker_input").instance(2)'
    )

    YEAR_PICKER_SCROLL = (
        'new UiScrollable('
        'new UiSelector().className("android.widget.NumberPicker").instance(2))'
        '.setAsVerticalList()'
        '.scrollBackward()'
    )

    AGE_NEXT_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/age_next_button')

    GENDER_LOCATORS = {
        "female": (AppiumBy.ID, 'com.spotify.music:id/gender_button_female'),
        "male": (AppiumBy.ID, 'com.spotify.music:id/gender_button_male'),
        "neutral": (AppiumBy.ID, 'com.spotify.music:id/gender_button_neutral'),
        "other": (AppiumBy.ID, 'com.spotify.music:id/gender_button_other'),
        "prefer_not_to_say": (AppiumBy.ID, 'com.spotify.music:id/gender_button_prefer_not_say'),
    }
    # no next button in gender screen

    USERNAME_INPUT = (AppiumBy.ID, 'com.spotify.music:id/name')
#username + marketing in one screem
    AGREE_TERMS_SWITCH = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.spotify.music:id/switch_agree").instance(0)'
    )

    AGREE_MARKETING_SWITCH = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.spotify.music:id/switch_agree").instance(1)'
    )
    CREATE_ACCOUNT_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/name_next_button') # need to click to create acc
    DECLINE_NOTIFICATION_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/decline')
    #account created, need to select min 3 artists
    SEARCH_FIELD = (AppiumBy.ID, 'com.spotify.music:id/search_field_root')
    SEARCH_INPUT = (AppiumBy.ID, 'com.spotify.music:id/query')
    ARTIST_BY_NAME_TEMPLATE = 'new UiSelector().text("{}")' # todo вынести в post sign up класс
    FIRST_SUGGESTED_ARTIST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.spotify.music:id/row_root").instance(0)')


    DONE_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/actionButton')
    NOT_NOW_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/secondary_button') # can be not used
    PRIMARY_BUTTON = (AppiumBy.ID, 'com.spotify.music:id/primary_button') # used to click start listening and then if displayed = user is logged in?

    #final to check user is logged in
    GO_TO_PROFILE_SETTINGS = (AppiumBy.ACCESSIBILITY_ID, 'Go to profile and settings')


class SignUpErrorLocatorsAndroid:
    """Locators for signup error messages"""

    EMAIL_ERROR_MESSAGE = (AppiumBy.ID, 'com.spotify.music:id/email_error_message')
    PASSWORD_ERROR_MESSAGE = (AppiumBy.ID, 'com.spotify.music:id/password_error_message')

