from config.database import db
from models.employee import Employee


class EmployeeService:
    def __init__(
        self,
        employee_dao,
        user_dao,
        department_dao,
        designation_dao
    ):
        self.employee_dao = employee_dao
        self.user_dao = user_dao
        self.department_dao = department_dao
        self.designation_dao = designation_dao

    def get_all(self):
        return self.employee_dao.get_all()

    def get_by_id(self, employee_id):
        employee = self.employee_dao.get_by_id(employee_id)
        if employee is None:
            raise ValueError("Employee not found")
        return employee

    def add_employee(self, data):
        required_fields = [
            "user_id",
            "full_name",
            "phone",
            "address",
            "department_id",
            "designation_id"
        ]

        for field in required_fields:
            if field not in data:
                raise ValueError(f"{field} is required")

        if not data["full_name"].strip():
            raise ValueError("Full name cannot be empty")

        if not data["phone"].strip():
            raise ValueError("Phone cannot be empty")

        if not data["address"].strip():
            raise ValueError("Address cannot be empty")

        user = self.user_dao.get_by_id(data["user_id"])
        if user is None:
            raise ValueError("User not found")

        existing_employee = self.employee_dao.get_by_user_id(data["user_id"])
        if existing_employee:
            raise ValueError("Employee already exists for this user")

        existing_phone = self.employee_dao.get_by_phone(data["phone"])
        if existing_phone:
            raise ValueError("Phone number already registered")

        department = self.department_dao.get_by_id(data["department_id"])
        if department is None:
            raise ValueError("Department not found")

        designation = self.designation_dao.get_by_id(data["designation_id"])
        if designation is None:
            raise ValueError("Designation not found")

        employee = Employee(
            user_id=data["user_id"],
            full_name=data["full_name"],
            phone=data["phone"],
            address=data["address"],
            department_id=data["department_id"],
            designation_id=data["designation_id"]
        )

        self.employee_dao.add(employee)
        db.session.commit()
        return employee

    def update_employee(self, employee_id, data):
        employee = self.employee_dao.get_by_id(employee_id)
        if employee is None:
            raise ValueError("Employee not found")

        if "full_name" in data:
            if not data["full_name"].strip():
                raise ValueError("Full name cannot be empty")
            employee.full_name = data["full_name"]

        if "phone" in data:
            if not data["phone"].strip():
                raise ValueError("Phone cannot be empty")

            existing_phone = self.employee_dao.get_by_phone(data["phone"])
            if existing_phone and existing_phone.id != employee.id:
                raise ValueError("Phone number already registered")
            employee.phone = data["phone"]

        if "address" in data:
            if not data["address"].strip():
                raise ValueError("Address cannot be empty")
            employee.address = data["address"]

        if "department_id" in data:
            department = self.department_dao.get_by_id(data["department_id"])
            if department is None:
                raise ValueError("Department not found")
            employee.department_id = data["department_id"]

        if "designation_id" in data:
            designation = self.designation_dao.get_by_id(data["designation_id"])
            if designation is None:
                raise ValueError("Designation not found")
            employee.designation_id = data["designation_id"]

        db.session.commit()
        return employee

    def delete_employee(self, employee_id):
        employee = self.employee_dao.get_by_id(employee_id)
        if employee is None:
            raise ValueError("Employee not found")

        db.session.delete(employee)
        db.session.commit()