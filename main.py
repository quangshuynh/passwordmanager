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
    def entry(fileName:str)->None: #processes the user name and password
        usr = input("Please enter the new user name:\n")
        with open(fileName + ".txt", "w+") as newUser:
            newUser.write(usr + "\n")
            print("\tsuccess in recording user name in specified user file")
            pw = input("Now please enter the new password:\n")
            newUser.write(pw)
            print("\tsuccess in recording password in specified user file")
    def create_new_user(self)->None: #the main method called to create a new user file
        confirm = input("Are you sure? Y or N:\n")
        if confirm == "Y":
            userName = input("Input new user name here:\n")
            #need file name input validation check here, make it eventually lol
            FileEditor.create_text_file(userName)
            FileEditor.entry(userName)
        else:
            print("Bye")
            exit(0)


#testing create_new_user, entry, and create_text_file
FileEditor.create_new_user(FileEditor)

#testing delete_file
FileEditor.delete_file("poop.txt")

# debugging
pm = PasswordManager()
pm.make_key("testkey.key")