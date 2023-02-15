#!/usr/bin/env python3
"""AUTH module
"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user if does not already exist
        Return:
            User object else
            Raise ValueError if already registered
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            return self._db.add_user(
                email=email, hashed_password=_hash_password(password)
            )

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate password if email exists
        Return True if valid else False
        """
        try:
            user_obj = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user_obj.hashed_password)
        except NoResultFound:
            return False


def _hash_password(password: str) -> bytes:
    """Hashes Password
    Return:
        A salted hash of the Input password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
