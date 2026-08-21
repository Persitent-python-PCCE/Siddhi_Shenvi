from config.database import db
from models.attendance import Attendance
class AttendanceDAO:
    def get_by_employee_and_date(self, employee_id, date):
        return Attendance.query.filter_by(
            employee_id=employee_id,
            date=date
        ).first()

    def get_by_employee(self, employee_id):
        return Attendance.query.filter_by(employee_id=employee_id).all()

    def add(self, attendance):
        db.session.add(attendance)

"""
    def update(self, attendance):
        db.session.commit()
        return attendance
"""