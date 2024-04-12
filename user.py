"""
Module to generate random users
"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent  # parent in our case represent our directory project
logging.basicConfig(filename=BASE_DIR / 'user.log', # logging with the absolute path from user.log to user.py
                    level=logging.DEBUG)
fake = faker.Faker()


def get_user():
    """ Generate a user
    :return: str(user)
    """
    logging.info("Generating user")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n):
    logging.info("Generating a of users")
    users = []
    for i in range(n):
        users.append(get_user())

    return users


def get_users_v2(n):
    """
     Generate list of Users
    :param int n:number of users
    :list[str]: (users)
    """
    users = []
    for _ in range(n):  # i replace with _
        users.append(get_user())

    return users


def get_users_v3(n):
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    users = get_users(n=5)
    print(users)
