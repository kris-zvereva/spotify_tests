from faker import Faker
import random
import string
from model.enums.user_gender import Gender

fake = Faker()


def _generate_random_email():
    """Generates random email with real domain"""
    return fake.email()


def _generate_random_password():
    """
    Generates password with requirements:
    - Minimum 10 characters
    - At least 1 letter
    - At least 1 digit or special character
    """
    # Base part: letters + digits (8 characters)
    letters = ''.join(random.choices(string.ascii_letters, k=6))
    digits = ''.join(random.choices(string.digits, k=2))

    # Special characters (2 characters)
    special_chars = '#?!&@$%'
    specials = ''.join(random.choices(special_chars, k=2))

    # Combine and shuffle
    password_list = list(letters + digits + specials)
    random.shuffle(password_list)

    return ''.join(password_list)


def _generate_random_username():
    """Generates random username"""
    return fake.user_name()


def _generate_random_birthday():
    """
    Generates random birthdate (age 21-25 years)
    Returns dict with day, month, year
    """
    # Random date between 21 and 25 years old
    random_date = fake.date_of_birth(minimum_age=21, maximum_age=25)

    return {
        'day': str(random_date.day),
        'month': random_date.strftime('%B'),
        'year': '2003'
    }


def _generate_random_gender():
    """Generates random gender from enum"""
    return random.choice(list(Gender)).value


def generate_test_user():
    """
    Generates complete test user data

    Returns:
        dict: {
            'email': str,
            'password': str,
            'username': str,
            'birthday': dict,
            'gender': str
        }
    """
    return {
        'email': _generate_random_email(),
        'password': _generate_random_password(),
        'username': _generate_random_username(),
        'birthday': _generate_random_birthday(),
        'gender': _generate_random_gender()
    }

INVALID_PASSWORDS = {
    'too_short': 'Short1!',
    'no_letter': '1234567890#',
    'no_number_or_special': 'OnlyLetters',
    'all_violated': '',
}

INVALID_BIRTHDAYS = {
    'invalid_day': {'day': '90', 'month': 'January', 'year': '1996'},
    'invalid_year': {'day': '15', 'month': 'January', 'year': '90'},
    'missing_month': {'day': '15', 'month': None, 'year': '1990'},
}
ARTISTS = ['System Of A Down', 'Sofia Isella', 'Noga Erez']