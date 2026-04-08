class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username: str, password: str) -> bool:
        if username in self.users:
            print("Username already exists.")
            return False
        self.users[username] = User(username, password)
        print(f"User {username} registered successfully.")
        return True

    def validate_user(self, username: str, password: str) -> bool:
        user = self.users.get(username)
        if user and user.password == password:
            return True
        return False

class LoginSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.login_attempts = 0

    def display_menu(self):
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                break
            else:
                print("Invalid option. Try again.")

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.user_manager.register_user(username, password)

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.user_manager.validate_user(username, password):
            print(f"Welcome {username}!")
            self.login_attempts = 0
        else:
            self.login_attempts += 1
            print("Invalid credentials.")
            if self.login_attempts >= 3:
                print("Too many failed attempts. Exiting...")
                exit()

if __name__ == '__main__':
    login_system = LoginSystem()
    login_system.display_menu()