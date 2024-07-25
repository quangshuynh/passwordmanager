"""
Password Manager Project
06/22/24
author: Quang Huynh, Kai Fan
"""
import os
# used to create and edit files and folders

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

class FileEditor:
    def create_text_file(fileName:str)->None: #this method overrides file with same name!
        print('Creating a new text file: "' + fileName + '"')
        with open(fileName + ".txt", "w") as newFile:
            pass
    def delete_file(fileName:str)->None: #careful with this method, it deletes things other than txt file
        print('Deleting file: "' + fileName + '"')
        try:
            os.remove(fileName)
        except PermissionError:
            print("Permission denied")
    #def create_new_user(): ###Waiting for response KF
        #with open()

#testing create_text_file
FileEditor.create_text_file("poop")

#testing delete_file
FileEditor.delete_file("poop.txt")

# debugging
pm = PasswordManager()
pm.make_key("testkey.key")