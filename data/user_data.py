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
        'gender': _generate_random_gender(),
        'birthday': {'day': '14', 'month': 'October', 'year': '2003'},
        'artists': ['System Of A Down', 'Sofia Isella', 'Noga Erez'],
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

TRACK_1_SEARCH_PARAMS = {
    'q': 'track:DUMB artist:Noga Erez',
    'type': 'track',
    'limit': 1
}

TRACK_2_SEARCH_PARAMS = {
    'q': 'track:The Doll People artist:SOFIA ISELLA',
    'type': 'track',
    'limit': 1
}


PLAYLIST_INFO = {
    "name": "The Coolest Playlist",
    "description": "I've died like 7 times while making it",
    "public": False
}

TRACK_IDS = {
    'NOGA_EREZ_DUMB': {
        'id': '2Pul6SaLL8e0sQhJDBVOr1',
        'album': 'THE VANDALIST',
        'explicit': False
    },
    'SOFIA_ISELLA_DOLL': {
        'id': '3GxyBdCpCeY2PvYdTL0fd4',
        'album': 'I Can Be Your Mother',
        'explicit': True
    }
}