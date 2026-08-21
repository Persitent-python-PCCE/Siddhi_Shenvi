from config.database import db
from models.user import User
from models.employee import Employee
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app

class AuthService:
    def __init__(self, user_dao, employee_dao):
        self.user_dao = user_dao
        self.employee_dao = employee_dao

    def register(self, data):
        username = data["username"]
        email = data["email"]
        password = data["password"]
        full_name = data["full_name"]
        phone = data["phone"]
        address = data["address"]
        department_id = data["department_id"]
        designation_id = data["designation_id"]

        if self.user_dao.get_by_username(username):
            raise ValueError("Username already registered")

        if self.user_dao.get_by_email(email):
            raise ValueError("Email already exists")

        if self.employee_dao.get_by_phone(phone):
            raise ValueError("Phone number already registered")

        hash_password = generate_password_hash(password)

        user = User(username=username, email=email, password=hash_password, role="EMPLOYEE", is_active=True)
        user = self.user_dao.add(user)
        db.session.flush()

        employee = Employee(
            user_id = user.id,
            full_name = full_name,
            phone = phone,
            address = address,
            department_id = department_id,
            designation_id = designation_id
        )
        self.employee_dao.add(employee)
        try:
            db.session.commit()

        except Exception:
            db.session.rollback()
            raise

        return employee

    def login(self, email, password):
        user = self.user_dao.get_by_email(email)
        if user is None:
            raise ValueError("Invalid email or password") 

        if not check_password_hash(user.password, password):
            raise ValueError("Invalid password or password")

        if not user.is_active:
            raise ValueError("User account is inactive")
        #jwt
        payload = {
            "sub": str(user.id),
            "role": user.role,
            "exp": datetime.now(timezone.utc) + timedelta(hours=1)
        }
        #signing token
        token = jwt.encode(
            payload,
            current_app.config["SECRET_KEY"],
            algorithm="HS256"
        )

        return token