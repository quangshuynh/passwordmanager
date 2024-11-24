"""
Password Manager Project
06/22/24
author: Quang Huynh, Kai Fan
"""

import os  # used to create and edit files and folders
from cryptography.fernet import Fernet  # used to encrypt passwords
import customtkinter as ctk  # for gui
from tkinter import messagebox  # for gui
from tkinter import simpledialog  # for gui

class PasswordManager:
    """
    A class to manage passwords securely using encryption.

    Attributes:
        key (bytes): The encryption key used for encrypting and decrypting passwords.
        pw_file (str): The file where encrypted passwords are stored.
        pw_dict (dict): A dictionary storing website-user-password tuples in memory.
    """
    def __init__(self):
        """Initializes the PasswordManager with default values."""
        self.key = None
        self.pw_file = "passwords.txt"
        self.pw_dict = {}
        self.load_passwords()

    def make_key(self, key_path="key.key"):
        """
        Generates or loads an encryption key from a file.

        Args:
            key_path (str): The path to the key file. Default is 'key.key'.

        Returns:
            None
        """
        if not os.path.exists(key_path):
            self.key = Fernet.generate_key()
            with open(key_path, "wb") as file:
                file.write(self.key)
            print("Key created and saved.")
        else:
            with open(key_path, "rb") as file:
                self.key = file.read()

    def load_passwords(self):
        """
        Loads and decrypts passwords from the password file.

        Returns:
            None
        """
        if os.path.exists(self.pw_file):
            with open(self.pw_file, "rb") as file:
                encrypted_data = file.read()
                try:
                    fernet = Fernet(self.key)
                    decrypted_data = fernet.decrypt(encrypted_data).decode()
                    for line in decrypted_data.split("\n"):
                        if line.strip():
                            website, user, password = line.split(":")
                            self.pw_dict[website] = (user, password)
                except Exception as e:
                    print("Error decrypting passwords:", e)

    def save_passwords(self):
        """
        Encrypts and saves passwords to the password file.

        Returns:
            None
        """
        fernet = Fernet(self.key)
        data = "\n".join(
            [f"{website}:{user}:{pw}" for website, (user, pw) in self.pw_dict.items()]
        )
        encrypted_data = fernet.encrypt(data.encode())
        with open(self.pw_file, "wb") as file:
            file.write(encrypted_data)

    def add_password(self, website, user, password):
        """
        Adds a new website-user-password tuple to the password dictionary and saves it.

        Args:
            website (str): The name of the website or application.
            user (str): The username for the website/application.
            password (str): The password associated with the username.

        Returns:
            None
        """
        self.pw_dict[website] = (user, password)
        self.save_passwords()

    def get_passwords(self):
        """
        Retrieves all stored passwords.

        Returns:
            dict: A dictionary containing website-user-password tuples.
        """
        return self.pw_dict

class PasswordManagerGUI:
    """
    A class to provide a graphical user interface for the PasswordManager.

    Attributes:
        pm (PasswordManager): An instance of the PasswordManager class.
        root (tk.Tk): The root window for the GUI.
    """
    def __init__(self, root):
        """
        Initializes the GUI application.

        Args:
            root (tk.Tk): The root window for the GUI.
        """
        self.pm = PasswordManager()
        self.pm.make_key()

        # configure root window
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x300")
        ctk.set_appearance_mode("dark")  # modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # themes: "blue" (default), "green", "dark-blue"

        # header label
        self.header_label = ctk.CTkLabel(
            root, text="Password Manager", font=("Roboto", 24, "bold")
        )
        self.header_label.pack(pady=20)

        # add Password Button
        self.add_button = ctk.CTkButton(
            root, text="Add Password", command=self.add_password, width=200
        )
        self.add_button.pack(pady=10)

        # view Passwords Button
        self.view_button = ctk.CTkButton(
            root, text="View Passwords", command=self.view_passwords, width=200
        )
        self.view_button.pack(pady=10)

        # quit Button
        self.quit_button = ctk.CTkButton(
            root, text="Quit", command=root.quit, fg_color="red", width=200
        )
        self.quit_button.pack(pady=10)

    def add_password(self):
        """
        Prompts the user to add a new password with an associated website/application.

        Opens dialog boxes to input a website name, username, and password, and stores them in the PasswordManager.

        Returns:
            None
        """
        website = simpledialog.askstring("Input", "Enter website/application name:")
        if not website:
            messagebox.showwarning("Warning", "Website/Application name cannot be empty!")
            return

        user = simpledialog.askstring("Input", "Enter username:")
        if not user:
            messagebox.showwarning("Warning", "Username cannot be empty!")
            return

        password = simpledialog.askstring("Input", "Enter password:")
        if not password:
            messagebox.showwarning("Warning", "Password cannot be empty!")
            return

        self.pm.add_password(website, user, password)
        messagebox.showinfo("Success", "Password added successfully!")

    def view_passwords(self):
        """
        Displays all stored passwords in a message box.

        If no passwords are stored, a message box indicates that no passwords exist.

        Returns:
            None
        """
        passwords = self.pm.get_passwords()
        if not passwords:
            messagebox.showinfo("Passwords", "No passwords stored yet!")
        else:
            pw_list = "\n".join(
                [f"{website}:\n User: {user}, Password: {pw}\n" for website, (user, pw) in passwords.items()]
            )
            messagebox.showinfo("Passwords", pw_list)

# run application
if __name__ == "__main__":
    root = ctk.CTk()
    gui = PasswordManagerGUI(root)
    root.mainloop()