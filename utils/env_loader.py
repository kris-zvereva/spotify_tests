from dotenv import find_dotenv, load_dotenv


def load_env(filename: str):
    """Find and load .env file"""
    env_file = find_dotenv(filename, usecwd=True)

    if not env_file:
        raise FileNotFoundError(f"{filename} not found")

    load_dotenv(env_file)
