#!/usr/bin/env python3
"""A module that returns the log message obfuscated"""

from typing import List
import re

# for field in fields:
#     # message = re.sub(f"(?<={field}=)[^{seperator}]*", redaction, message)
#     message = re.sub(f"{field}=[^{seperator}]*", redaction, message)
# return message


def filter_datum(
    fields: List[str], redaction: str, message: str, seperator: str
) -> str:
    """obfuscating function"""
    pat = '(?P<nm>' + '=|'.join(fields) + '=)' + f'[^{separator}]+{separator}'
    return re.sub(pat, r"\g<nm>{}{}".format(redaction, separator), message)
