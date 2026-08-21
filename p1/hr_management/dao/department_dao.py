from config.database import db
from models.department import Department


class DepartmentDAO:

    def get_all(self):
        return Department.query.all()

    def get_by_id(self, department_id):
        return Department.query.get(department_id)

    def add(self, department):
        db.session.add(department)

    def delete(self, department):
            db.session.delete(department)
            db.session.commit()

"""
    def get_by_name(self, name):
        return Department.query.filter_by(name=name).first()

    def update(self, department):
        db.session.commit()
        return department
"""

    