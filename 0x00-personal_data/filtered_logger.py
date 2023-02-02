#!/usr/bin/env python3
"""A module that returns the log message obfuscated"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: List[str], seperator: str):
    """obfuscating function"""
    for field in fields:
        message = re.sub(r"(?<={}=)[\d\w\/\\.?]*(?<!{})".format(field, seperator), redaction, message)
    return message
