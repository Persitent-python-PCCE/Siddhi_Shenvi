from datetime import date

from config.database import db
from models.leave_requests import LeaveRequest


class LeaveRequestService:
    def __init__(self, leave_request_dao, employee_dao, leave_type_dao, leave_balance_dao):
        self.leave_request_dao = leave_request_dao
        self.employee_dao = employee_dao
        self.leave_type_dao = leave_type_dao
        self.leave_balance_dao = leave_balance_dao

    def apply_leave(self, user_id, data):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")

        if "leave_type_id" not in data:
            raise ValueError("Leave type is required")
        if "start_date" not in data:
            raise ValueError("Start date is required")
        if "end_date" not in data:
            raise ValueError("End date is required")

        leave_type = self.leave_type_dao.get_by_id(data["leave_type_id"])
        if leave_type is None:
            raise ValueError("Leave type not found")

        start_date = date.fromisoformat(data["start_date"])
        end_date = date.fromisoformat(data["end_date"])

        if end_date < start_date:
            raise ValueError("End date cannot be before start date")

        leave_request = LeaveRequest(
            employee_id=employee.id,
            leave_type_id=data["leave_type_id"],
            start_date=start_date,
            end_date=end_date,
            reason=data.get("reason"),
            status="PENDING"
        )

        self.leave_request_dao.add(leave_request)
        db.session.commit()
        return leave_request

    def get_my_requests(self, user_id):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")

        return self.leave_request_dao.get_by_employee(employee.id)

    def approve_leave(self, request_id, user_id):
        leave_request = self.leave_request_dao.get_by_id(request_id)
        if leave_request is None:
            raise ValueError("Leave request not found")

        if leave_request.status != "PENDING":
            raise ValueError("Leave request has already been processed")

        start_date = leave_request.start_date
        leave_days = (end_date - start_date).days + 1

        balance = self.leave_balance_dao.get_by_employee_and_leave_type(
            leave_request.employee_id,
            leave_request.leave_type_id
        )

        if balance is None:
            raise ValueError("Leave balance not found")

        if balance.remaining_days < leave_days:
            raise ValueError("Insufficient leave balance")

        balance.used_days += leave_days
        balance.remaining_days -= leave_days

        leave_request.status = "APPROVED"
        leave_request.approved_by = user_id

        db.session.commit()
        return leave_request

    def reject_leave(self, request_id):
        leave_request = self.leave_request_dao.get_by_id(request_id)

        if leave_request is None:
            raise ValueError("Leave request not found")

        if leave_request.status != "PENDING":
            raise ValueError("Leave request has already been processed")

        leave_request.status = "REJECTED"
        self.leave_request_dao.update(leave_request)

        return leave_request

    