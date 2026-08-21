from dao.user_dao import UserDAO
from model.user import User


class UserService:

    def __init__(self):
        self.user_dao = UserDAO()

    def add_user(self, user):

        if not user.name.strip():
            raise ValueError("Name cannot be empty.")

        if not user.email.strip():
            raise ValueError("Email cannot be empty.")

        if "@" not in user.email or "." not in user.email:
            raise ValueError("Invalid email format.")

        if not user.password:
            raise ValueError("Password cannot be empty.")

        if len(user.password) < 6:
            raise ValueError(
                "Password must contain at least 6 characters."
            )

        user.name = user.name.strip()
        user.email = user.email.strip()

        if self.user_dao.email_exists(user.email):
            raise ValueError("Email is already registered.")

        user.role = "customer"

        return self.user_dao.add_user(user)

    def login_user(self, email, password):

        if not email.strip():
            raise ValueError("Email cannot be empty.")

        if not password:
            raise ValueError("Password cannot be empty.")

        email = email.strip()

        user_data = self.user_dao.get_user_by_email(email)

        if user_data is None:
            raise ValueError("Invalid email or password.")

        user_id, name, user_email, stored_password, role = user_data

        if password != stored_password:
            raise ValueError("Invalid email or password.")

        return User(
            user_id,
            name,
            user_email,
            stored_password,
            role
        )