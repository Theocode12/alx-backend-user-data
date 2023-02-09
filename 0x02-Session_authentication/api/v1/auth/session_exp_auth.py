#!/usr/bin/env python3
"""
Creation of the SessionExpAuth class to
set the expiration date of a session
"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv

class SessionExpAuth(SessionAuth):
    """
    A class that implements the session
    duration
    """
    def __init__(self):
        """Initializer"""
        # self.session_duration = getenv('SESSION_DURATION') ?  :
        