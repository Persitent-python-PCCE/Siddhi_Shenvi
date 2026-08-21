from config.database import db
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    is_active =  db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            "id":self.id,
            "username":self.username,
            "email":self.email,
            "role":self.role,
            "is_active":self.is_active
        }