from config.database import db
from models.leave_balances import LeaveBalance


class LeaveBalanceDAO:
    def get_by_employee_and_leave_type(self, employee_id, leave_type_id):
        return LeaveBalance.query.filter_by(
            employee_id=employee_id,
            leave_type_id=leave_type_id
        ).first()

    def get_by_employee(self, employee_id):
        return LeaveBalance.query.filter_by(employee_id=employee_id).all()

    def add(self, balance):
        db.session.add(balance)