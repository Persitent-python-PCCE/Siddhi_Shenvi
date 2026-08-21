from models.user import User
from config.database import db

class UserDAO:

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def add(self, user):
        db.session.add(user)

        return user