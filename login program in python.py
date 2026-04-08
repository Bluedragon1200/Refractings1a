import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {"user1": hash_password("password1"), "user2": hash_password("password2")}

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
        return True
    else:
        print("Invalid credentials.")
        return False
