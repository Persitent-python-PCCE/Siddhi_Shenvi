from config.database import db
from models.designation import Designation

class DesignationDAO:

    def get_all(self):
        return Designation.query.all()

    def get_by_id(self, designation_id):
        return Designation.query.get(designation_id)

    def add(self, designation):
        db.session.add(designation)

    def delete(self, designation):
            db.session.delete(designation)
            db.session.commit()
"""
     def get_by_name(self, name):
            return Designation.query.filter_by(name=name).first()

    def update(self, designation):
        db.session.commit()
        return designation
"""

    