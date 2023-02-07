#!/usr/bin/env python3
""" Creationof the Auth class """

from flask import request
from typing import List, TypeVar


class Auth(object):
    """Auth class that mimicks HTTP Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if the given path requires authentication
        by checking the excluded paths
        Returns:
            True if the path is not in the exlcuded path
            False if the path is in the excluded path
        """
        if path and excluded_paths:
            if path.endswith("/"):
                npath = path[:-1]
            else:
                npath = path + "/"
            for ex_path in excluded_paths:
                if (
                    (
                        ex_path.endswith("*")
                        and path.startswith(ex_path.rstrip("*"))
                    )
                    or path == ex_path
                    or npath == ex_path
                ):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Validate all request to secure the API
        Return:
            None if request is None
            Value of the Authorization header if found
        """
        if request and request.headers.get("Authorization"):
            return request.headers.get("Authorization")
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """Overload auth and retrive a User istance from a request
        Return:
            Retrives a user instance if possible
        """
        return None
