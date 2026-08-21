from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from config.database import db, init_db
from controller.auth_controller import auth_controller
from controller.employee_controller import employee_controller
from controller.department_controller import department_controller
from controller.designation_controller import designation_controller
from controller.attendance_controller import attendance_controller
from controller.leave_type_controller import leave_type_controller
from controller.employee_documents_controller import employee_documents_controller
from controller.leave_request_controller import leave_request_controller
load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

init_db(app)

app.register_blueprint(auth_controller)
app.register_blueprint(employee_controller)
app.register_blueprint(department_controller)
app.register_blueprint(designation_controller)
app.register_blueprint(attendance_controller)
app.register_blueprint(leave_type_controller)
app.register_blueprint(leave_request_controller)
app.register_blueprint(employee_documents_controller)

# Import all models so SQLAlchemy knows about them
from models.employee import Employee
from models.department import Department
from models.designation import Designation
from models.attendance import Attendance
from models.leave_types import LeaveTypes
from models.leave_requests import LeaveRequest
from models.leave_balances import LeaveBalance
from models.employee_documents import EmployeeDocuments


@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "not found"
    }), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({
        "error": "internal server error"
    }), 500

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)