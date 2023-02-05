#!/usr/bin/env python3
"""A module that returns the log message obfuscated"""

from typing import List
import logging
import re


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """obfuscating function"""
    for field in fields:
        message = re.sub(f"(?<={field}=)[^{separator}]*", redaction, message)
        # message = re.sub(f"{field}=[^{separator}]*", redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """formats logger information"""
        message = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        record.msg = message
        return super().format(record)
