from config.database import db
from models.leave_types import LeaveTypes

class LeaveTypeDAO:

    def get_all(self):
        return LeaveTypes.query.all()

    def get_by_id(self, leave_type_id):
        return LeaveTypes.query.get(leave_type_id)

    def add(self, leave_type):
        db.session.add(leave_type)

    def delete(self, leave_type):
        db.session.delete(leave_type)
        db.session.commit()
        
"""
    def update(self, leave_type):
            db.session.commit()
            return leave_type
    
    def get_by_name(self, name):
            return LeaveTypes.query.filter_by(
                name=name
            ).first()
"""