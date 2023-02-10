#!/usr/bin/env python3
"""
Creation of the SessionDbAuth class
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDbAuth(SessionExpAuth):
    """A class that manages saving the session"""

    def create_session(self, user_id=None) -> str:
        """create a new session
        Returns:
            A session id"""
        session_id = super().create_session(user_id)
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None) -> str:
        """Returns the User ID by requesting UserSession in the database
        based on session_id
        """
        user_id = super().user_id_for_session_id(session_id)
        # if not user_id:
        #     UserSession.load_from_file()
        #     user_session_obj = UserSession.search({'session_id': session_id})
        #     if user_session_obj:
        #         user_id = user_session_obj[0].user_id
        #     else:
        #         user_id = None
        return user_id

    def destroy_session(self, request=None):
        """Destroy session based on request cookie"""
        if super().destroy_session(request):
            session_id = self.session_cookie(request)
            user_session_obj = UserSession.search({"session_id": session_id})
            user_session_obj[0].remove()
