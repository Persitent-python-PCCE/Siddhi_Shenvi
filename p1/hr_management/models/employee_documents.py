from config.database import db

class EmployeeDocuments(db.Model):
    __tablename__ = "employee_documents"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
    document_type = db.Column(db.String(50), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
           "id": self.id,
            "employee_id": self.employee_id,
            "document_type": self.document_type,
            "file_name": self.file_name,
            "file_size": self.file_size,
        }


    