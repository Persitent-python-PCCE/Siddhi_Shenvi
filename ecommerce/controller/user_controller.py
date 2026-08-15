from model.user import User
from service.user_service import UserService


class UserController:

    def __init__(self):
        self.user_service = UserService()

    def add_user(self):

        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        user = User(
            None,
            name,
            email,
            password,
            "customer"
        )

        try:

            user = self.user_service.add_user(user)

            print("\nUser registered successfully!")
            print("User ID:", user.user_id)
            print("Role:", user.role)

        except ValueError as error:

            print("\nRegistration failed:", error)

        except Exception as error:

            print("\nSomething went wrong:", error)

    def login_user(self):

        email = input("Enter email: ")
        password = input("Enter password: ")

        try:

            user = self.user_service.login_user(
                email,
                password
            )

            print("\nLogin successful!")
            print("Welcome,", user.name)
            print("Role:", user.role)

            return user

        except ValueError as error:

            print("\nLogin failed:", error)

            return None