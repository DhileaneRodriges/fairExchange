"""
title           : encdec.py
description     : 
                :
source          : 
                : https://blog.gitnux.com/code/python-o
                : penssl/#:~:text=You%20can%20use%20OpenSSL%2
                : 0in,%2C%20digital%20certificates%2C%20and%20more.
                :
                : https://pypi.org/project/cryptography/3.4.8/
                : pip install cryptography==3.4.8
                : https://cryptography.io/en/3.4.2/hazmat/primitives/
                :  key-derivation-functions.html
                : 
author          : Carlos Molina-Jimenez,
                : carlos.molina@cl.cam.ac.uk
date            : 10 Sep 2023, Computer Lab, University of Cambridge
version         : __ 
usage           : 
notes           :
compile and run : 
                :
                : bash-3.2$ py encdec.py
                : Encrypted data: b'gAAAAABk_Qwtlwu9pclTNsPABpT
                : ...
                : Decrypted data: Hello, let's encrypt this text.
python_version  : Python 3.7.4(v3.7.4:e09359112e, Jul 8 2019, 14:36:03) 
"""

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import padding
import os
import base64

def generate_key(password, salt=None):
    password = password.encode()
    if not salt:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key, salt


def encrypt(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data.decode()


if __name__ == "__main__":
    password = "my_secure_password"
    key, salt = generate_key(password)

    data = "Hello, let's encrypt this text."

    encrypted_data = encrypt(data, key)
    print("Encrypted data:", encrypted_data)

    decrypted_data = decrypt(encrypted_data, key)
    print("Decrypted data:", decrypted_data)


