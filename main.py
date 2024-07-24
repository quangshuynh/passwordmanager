"""
Password Manager Project
06/22/24
author: Quang Huynh, Kai Fan
"""
import os
# used to create a folder that holds all the files

from cryptography.fernet import Fernet
# used to encrypt passwords

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

class FileEdits:
    def create_file(fileName):
        print('Creating a new file: "' + fileName + '"')
        with open(fileName + ".txt", "w") as newFile:
            pass
    def delete_file(fileName):
        print("in development")

#testing create_file
FileEdits.create_file("poop")



# debugging
pm = PasswordManager()
pm.make_key("testkey.key")