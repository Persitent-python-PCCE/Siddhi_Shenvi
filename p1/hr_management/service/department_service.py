from config.database import db
from models.department import Department


class DepartmentService:
    def __init__(self, department_dao):
        self.department_dao = department_dao

    def get_all(self):
        return self.department_dao.get_all()

    def get_by_id(self, department_id):
        department = self.department_dao.get_by_id(department_id)
        if department is None:
            raise ValueError("Department not found")
        return department

    def add_department(self, data):
        if "name" not in data:
            raise ValueError("Name is required")

        if not data["name"].strip():
            raise ValueError("Department name cannot be empty")

        existing = self.department_dao.get_by_name(data["name"])
        if existing:
            raise ValueError("Department already exists")

        department = Department(name=data["name"])
        self.department_dao.add(department)
        db.session.commit()
        return department

    def update_department(self, department_id, data):
        department = self.department_dao.get_by_id(department_id)
        if department is None:
            raise ValueError("Department not found")

        if "name" not in data:
            raise ValueError("Name is required")

        if not data["name"].strip():
            raise ValueError("Department name cannot be empty")

        existing = self.department_dao.get_by_name(data["name"])
        if existing and existing.id != department.id:
            raise ValueError("Department already exists")

        department.name = data["name"]
        db.session.commit()
        return department

    def delete_department(self, department_id):
        department = self.department_dao.get_by_id(department_id)
        if department is None:
            raise ValueError("Department not found")

        db.session.delete(department)
        db.session.commit()