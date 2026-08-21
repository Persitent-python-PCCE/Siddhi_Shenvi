from config.database import db
from models.employee_documents import EmployeeDocuments


class EmployeeDocumentsDAO:

    def get_by_id(self, document_id):
        return EmployeeDocuments.query.get(document_id)

    def get_by_employee(self, employee_id):
        return EmployeeDocuments.query.filter_by(employee_id=employee_id).all()

    def add(self, document):
        db.session.add(document)

    def delete(self, document):
        db.session.delete(document)