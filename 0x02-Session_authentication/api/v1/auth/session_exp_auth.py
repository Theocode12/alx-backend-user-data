#!/usr/bin/env python3
"""
Creation of the SessionExpAuth class to
set the expiration date of a session
"""

from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta, time
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    A class that implements the session
    duration
    """

    ENV = getenv("SESSION_DURATION")

    def __init__(self):
        """Initializer"""
        try:
            self.session_duration = int(self.ENV) if self.ENV else 0
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None) -> str:
        """Creates a new session by calling
        the Super class's create_session method
        """
        session_id = super().create_session(user_id)
        if session_id:
            session_dictionary = {
                "user_id": user_id,
                "created_at": datetime.now(),
            }
            self.user_id_by_session_id[session_id] = session_dictionary
            return session_id
        return None

    def user_id_for_session_id(self, session_id=None):
        """
        Overload the superclass implementation of this
        method
        """
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_id and session_dict:
            if self.session_duration <= 0:
                return session_dict.get("user_id")
            if session_dict.get("created_at"):
                time_exp = session_dict.get("created_at") + timedelta(
                    seconds=self.session_duration
                )
                if time_exp >= datetime.now():
                    return session_dict.get("user_id")
            return None
        return None
