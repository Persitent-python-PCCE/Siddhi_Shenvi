from config.database import db

class LeaveTypes(db.Model):
    __tablename__ = "leave_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    max_days = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "max_days" : self.max_days
        }