#/usr/bin/env python3

import bcrypt   

def hash_password(password: str) > bytes:
    salt = bcrypt.gensalt()
    hashed_password =
byrypt.hashpw(password.encode() , salt)
    return hashed_password
