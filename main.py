"""
Password Manager Project
06/22/24
author: Quang Huynh, Kai Fan
"""

from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = None
        self.pw_file = None  # password file
        self.pw_dict = {}  # password dictionary

    def make_key(self, path):
        self.key = Fernet.generate_key()  # generate a key
        # print(self.key)
        with open(path, "wb") as file:
            file.write(self.key)

# debugging
pm = PasswordManager()
pm.make_key("testkey.key")
