from config.database import db
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = "attendance"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    date =  db.Column(db.Date, nullable=False)
    check_in = db.Column(db.DateTime, nullable=True)
    check_out = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default="PRESENT")

    def to_dict(self):
        return {
            "id" : self.id,
            "employee_id" : self.employee_id,
            "date" : str(self.date) if self.date else None,
            "check_in" : str(self.check_in) if self.check_in else None,
            "check_out" : str(self.check_out) if self.check_out else None,
            "status" : self.status
        }
    

