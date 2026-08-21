from config.database import db
from models.leave_types import LeaveTypes


class LeaveTypeService:
    def __init__(self, leave_type_dao):
        self.leave_type_dao = leave_type_dao

    def get_all(self):
        return self.leave_type_dao.get_all()

    def get_by_id(self, leave_type_id):
        return self.leave_type_dao.get_by_id(leave_type_id)

    def create(self, data):
        leave_type = LeaveTypes(name=data["name"])
        self.leave_type_dao.add(leave_type)
        db.session.commit()
        return leave_type

    def update(self, leave_type_id, data):
        leave_type = self.leave_type_dao.get_by_id(leave_type_id)
        leave_type.name = data["name"]
        db.session.commit()
        return leave_type

    def delete(self, leave_type_id):
        leave_type = self.leave_type_dao.get_by_id(leave_type_id)
        db.session.delete(leave_type)
        db.session.commit()