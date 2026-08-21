from datetime import date, datetime

from config.database import db
from models.attendance import Attendance


class AttendanceService:
    def __init__(self, attendance_dao, employee_dao):
        self.attendance_dao = attendance_dao
        self.employee_dao = employee_dao

    def check_in(self, user_id):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")

        today = date.today()
        existing = self.attendance_dao.get_by_employee_and_date(
            employee.id,
            today
        )
        if existing:
            raise ValueError("Already checked in today")

        attendance = Attendance(
            employee_id=employee.id,
            date=today,
            check_in=datetime.now(),
            status="PRESENT"
        )
        try:
            self.attendance_dao.add(attendance)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        return attendance

    def check_out(self, user_id):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")
        today = date.today()
        attendance = self.attendance_dao.get_by_employee_and_date(
            employee.id,
            today
        )

        if attendance is None:
            raise ValueError("You have not checked in today")
        if attendance.check_out is not None:
            raise ValueError("Already checked out today")
        attendance.check_out = datetime.now()
        try:
            self.attendance_dao.update(attendance)
        except Exception:
            db.session.rollback()
            raise
        return attendance

    def get_my_attendance(self, user_id):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")
        return self.attendance_dao.get_all_by_employee(employee.id)