#!/usr/bin/env python3
"""A module that returns the log message obfuscated"""

from typing import List
import re

# for field in fields:
#     # message = re.sub(f"(?<={field}=)[^{seperator}]*", redaction, message)
#     message = re.sub(f"{field}=[^{seperator}]*", redaction, message)
# return message


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscating function"""
    for field in fields:
        message = re.sub(f"(?<={field}=)[^{separator}]*", redaction, message)
        # message = re.sub(f"{field}=[^{separator}]*", redaction, message)
    return message
