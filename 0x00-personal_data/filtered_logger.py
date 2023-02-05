#!/usr/bin/env python3
"""A module that returns the log message obfuscated"""

from typing import List
import logging
import re

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Get the logger"""
    my_logger = logging.getLogger("user_data")
    my_logger.setLevel(logging.INFO)
    my_logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    return my_logger
