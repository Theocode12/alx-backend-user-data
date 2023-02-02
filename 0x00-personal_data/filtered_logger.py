#!/usr/bin/env python3
"""A module that returns the log message obfuscated"""

from typing import List
import re


def filter_datum(
    fields: List[str], redaction: str, message: str, seperator: str
) -> str:
    """obfuscating function"""
    for field in fields:
        message = re.sub(f"(?<={field}=)[^{seperator}]*", redaction, message)
    return message
