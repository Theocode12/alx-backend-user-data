#!/usr/bin/env python3
"""
Creationof the Session Auth class
"""

from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """
    A session auth class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a new session for the given user_id
        Return:
            session_id if successfully created
            else None
        """
        if user_id and isinstance(user_id, str):
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        searches the user_id_by_session_id for a user_id
        Returns:
            return user_id
            else None
        """
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None) -> str:
        """
        collect the session_id from the cookies and
        find the the user instance
        Return:
            the user instance
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """
        Destroys/Deletes a user session
        """
        session_id = self.session_cookie(request)
        if request and session_id and self.user_id_for_session_id(session_id):
            self.user_id_by_session_id.__delitem__(session_id)
            return True
        return False
