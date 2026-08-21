from config.database import db
from models.leave_requests import LeaveRequest

class LeaveRequestDAO:
    def get_by_id(self, request_id):
        return LeaveRequest.query.get(request_id)

    def get_by_employee(self, employee_id):
        return LeaveRequest.query.filter_by(employee_id=employee_id).all()

    def add(self, leave_request):
        db.session.add(leave_request)

    def update(self, leave_request):
        db.session.commit()