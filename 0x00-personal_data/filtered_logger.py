#!/usr/bin/env python3
"""A module that returns the log message obfuscated"""

from typing import List
import re


def filter_datum(
    fields: List[str], redaction: str, message: str, seperator: str
):
    """obfuscating function"""
    for field in fields:
        message = re.sub(
            r"(?<={}=)[^{}]*".format(field, seperator), redaction, message
        )
    return message
