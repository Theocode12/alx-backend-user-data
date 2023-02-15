#!/usr/bin/env python3
"""AUTH module
"""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


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

    def create_session(self, email: str) -> str:
        """
        Create a new session for a user
        Return:
            session id
        """
        try:
            user_obj = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user_obj.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get user from session id"""
        if session_id:
            try:
                user_obj = self._db.find_user_by(session_id=session_id)
                return user_obj
            except NoResultFound:
                pass
        return None


def _generate_uuid() -> str:
    """Generate a unique identifier"""
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """Hashes Password
    Return:
        A salted hash of the Input password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
