from config.database import db
from models.employee import Employee

class EmployeeDAO:
    def get_all(self):
        return Employee.query.all()

    def get_by_phone(self, phone):
        return Employee.query.filter_by(phone=phone).first()

    def get_by_id(self, employee_id):
        return Employee.query.get(employee_id)

    def get_by_user_id(self, user_id):
        return Employee.query.filter_by(user_id=user_id).first()

    def add(self, employee):
        db.session.add(employee)
       # db.session.commit()
       # return employee

    """ def update(self, employee):
        db.session.commit()
        return employee """

    def delete(self, employee):
        db.session.delete(employee)
        db.session.commit()

    """ def save(self, employee):
        db.session.add(employee) """