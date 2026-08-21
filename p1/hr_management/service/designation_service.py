from config.database import db
from models.designation import Designation

class DesignationService:
    def __init__(self, designation_dao, department_dao):
        self.designation_dao = designation_dao
        self.department_dao = department_dao

    def get_all(self):
        return self.designation_dao.get_all()

    def get_by_id(self, designation_id):
        designation = self.designation_dao.get_by_id(designation_id)
        if designation is None:
            raise ValueError("Designation not found")
        return designation

    def add_designation(self, data):
        if "name" not in data:
            raise ValueError("Name is required")

        if "department_id" not in data:
            raise ValueError("Department is required")

        if not data["name"].strip():
            raise ValueError("Designation name cannot be empty")

        department = self.department_dao.get_by_id(data["department_id"])
        if department is None:
            raise ValueError("Department not found")

        existing = self.designation_dao.get_by_name(data["name"])
        if existing:
            raise ValueError("Designation already exists")

        designation = Designation(
            name=data["name"],
            department_id=data["department_id"]
        )

        self.designation_dao.add(designation)
        db.session.commit()
        return designation

    def update_designation(self, designation_id, data):
        designation = self.designation_dao.get_by_id(designation_id)
        if designation is None:
            raise ValueError("Designation not found")

        if "name" in data:
            if not data["name"].strip():
                raise ValueError("Designation name cannot be empty")
            designation.name = data["name"]

        if "department_id" in data:
            department = self.department_dao.get_by_id(data["department_id"])
            if department is None:
                raise ValueError("Department not found")
            designation.department_id = data["department_id"]

        db.session.commit()
        return designation

    def delete_designation(self, designation_id):
        designation = self.designation_dao.get_by_id(designation_id)
        if designation is None:
            raise ValueError("Designation not found")

        db.session.delete(designation)
        db.session.commit()