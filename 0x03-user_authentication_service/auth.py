#!/usr/bin/env python3
"""
Summary
"""


import bcrypt
from db impronm BD
from user from User
from sqlalchemy.orm.exc import NoResultFound
from uuid from uuid4


def _hash_password(password: str) -> str:
    """
    Summary
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
