import os
import uuid

from werkzeug.utils import secure_filename

from config.database import db
from models.employee_documents import EmployeeDocuments


class EmployeeDocumentsService:
    ALLOWED_EXTENSIONS = {
        "pdf",
        "doc",
        "docx",
        "jpg",
        "jpeg",
        "png"
    }

    def __init__(self, documents_dao, employee_dao):
        self.documents_dao = documents_dao
        self.employee_dao = employee_dao

    def get_my_documents(self, user_id):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")

        return self.documents_dao.get_by_employee(employee.id)

    def upload_document(self, user_id, document_type, file):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")

        if not document_type:
            raise ValueError("Document type is required")

        if file is None:
            raise ValueError("File is required")

        if file.filename == "":
            raise ValueError("File name is required")

        filename = secure_filename(file.filename)
        if not filename:
            raise ValueError("Invalid file name")

        if "." not in filename:
            raise ValueError("File extension is required")

        extension = filename.rsplit(".", 1)[1].lower()
        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError("File type not allowed")

        upload_folder = "uploads/documents"
        os.makedirs(upload_folder, exist_ok=True)

        unique_name = f"{uuid.uuid4().hex}_{filename}"
        file_path = os.path.join(upload_folder, unique_name)

        file.save(file_path)
        file_size = os.path.getsize(file_path)

        document = EmployeeDocuments(
            employee_id=employee.id,
            document_type=document_type,
            file_name=filename,
            file_path=file_path,
            file_size=file_size
        )

        self.documents_dao.add(document)
        db.session.commit()

        return document

    def get_my_document(self, user_id, document_id):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")

        document = self.documents_dao.get_by_id(document_id)
        if document is None:
            raise ValueError("Document not found")

        if document.employee_id != employee.id:
            raise ValueError("You are not allowed to access this document")

        return document

    def delete_my_document(self, user_id, document_id):
        employee = self.employee_dao.get_by_user_id(user_id)
        if employee is None:
            raise ValueError("Employee not found")

        document = self.documents_dao.get_by_id(document_id)
        if document is None:
            raise ValueError("Document not found")

        if document.employee_id != employee.id:
            raise ValueError("You are not allowed to delete this document")

        if os.path.exists(document.file_path):
            os.remove(document.file_path)

        self.documents_dao.delete(document)
        db.session.commit()

    def get_employee_documents(self, employee_id):

        employee = self.employee_dao.get_by_id(employee_id)

        if employee is None:
            raise ValueError("Employee not found")

        return self.documents_dao.get_by_employee(
            employee_id
        )