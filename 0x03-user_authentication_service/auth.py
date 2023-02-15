#!/usr/bin/env python3
"""AUTH module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes Password
    Return:
        A salted hash of the Input password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
