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
