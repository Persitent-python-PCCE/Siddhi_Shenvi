from config.database import db
from datetime import date

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    address = db.Column(db.String(250), nullable=False)
    joining_date = db.Column(db.Date, default=date.today)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)
    designation_id = db.Column(db.Integer, db.ForeignKey("designations.id"), nullable=False)
    status = db.Column(db.String(20), default="ACTIVE")
    profile_photo = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "full_name": self.full_name,
            "phone": self.phone,
            "address": self.address,
            "joining_date": str(self.joining_date)
            if self.joining_date else None,
            "department_id": self.department_id,
            "designation_id": self.designation_id,
            "status": self.status,
            "profile_photo": self.profile_photo
        }