#!/usr/bin/env python3
"""
Module for filtering log data
"""
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): String to replace the field values with.
        message (str): Log message.
        separator (str): Separator used in the log message.

    Returns:
        str: Obfuscated log message.
    """
    pattern = '|'.join([
        f'(?<={field}=)[^{separator}]+' for field in fields
    ])
    return re.sub(pattern, redaction, message)



class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record with obfuscated sensitive information.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
