import unittest

from model.user import User
from service.user_service import UserService


class TestUserRegistration(unittest.TestCase):

    def setUp(self):

        self.user_service = UserService()

    def test_empty_name(self):

        user = User(
            None,
            "",
            "test@gmail.com",
            "123456",
            "customer"
        )

        with self.assertRaises(ValueError):
            self.user_service.add_user(user)

    def test_empty_email(self):

        user = User(
            None,
            "Siddhi",
            "",
            "123456",
            "customer"
        )

        with self.assertRaises(ValueError):
            self.user_service.add_user(user)

    def test_invalid_email(self):

        user = User(
            None,
            "Siddhi",
            "siddhi",
            "123456",
            "customer"
        )

        with self.assertRaises(ValueError):
            self.user_service.add_user(user)

    def test_empty_password(self):

        user = User(
            None,
            "Siddhi",
            "siddhi@gmail.com",
            "",
            "customer"
        )

        with self.assertRaises(ValueError):
            self.user_service.add_user(user)

    def test_short_password(self):

        user = User(
            None,
            "Siddhi",
            "siddhi@gmail.com",
            "123",
            "customer"
        )

        with self.assertRaises(ValueError):
            self.user_service.add_user(user)


if __name__ == "__main__":
    unittest.main()