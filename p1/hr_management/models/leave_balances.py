from config.database import db

class LeaveBalance(db.Model):
    __tablename__ = "leave_balances"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    leave_type_id = db.Column(db.Integer, db.ForeignKey("leave_types.id"), nullable=False)
    total_days = db.Column(db.Integer, nullable=False, default = 0)
    used_days =  db.Column(db.Integer, nullable=False, default = 0)
    remaining_days = db.Column(db.Integer, nullable=False, default = 0)

    def to_dict(self):
        return {
            "id" : self.id,
            "employee_id" : self.employee_id,
            "leave_type_id" : self.leave_type_id,
            "total_days": self.total_days,
            "used_days": self.used_days,
            "remaining_days": self.remaining_days
        }
