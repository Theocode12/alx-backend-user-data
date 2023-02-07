#!/usr/bin/env python3
""" Creation of the BasicAuth class """

from flask import request
from typing import List, TypeVar
from .auth import Auth


class BasicAuth(Auth):
    """A BasicAuth class"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """convert Authorization header to base64
        Returns:
            Base64 encoded string of authorization header
        """
        if (
            authorization_header
            and isinstance(authorization_header, str)
            and authorization_header.startswith("Basic ")
        ):
            return authorization_header.split()[1]

        return None
