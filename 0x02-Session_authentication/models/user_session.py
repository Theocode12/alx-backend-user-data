"""
A module that store our session in a database
"""

from models.base import Base


class UserSession(Base):
    """A class that models storage for
    user sessions
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Initializer for UserSession"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
