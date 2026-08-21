from flask import Blueprint, jsonify, request

from dao.employee_dao import EmployeeDAO
from service.authorization import role_required, token_required
from service.employee_service import EmployeeService

employee_controller = Blueprint("employee_controller", __name__)
employee_service = EmployeeService(EmployeeDAO())


@employee_controller.route("/api/employees", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_employees():
    employees = employee_service.get_all()
    return jsonify([employee.to_dict() for employee in employees]), 200


@employee_controller.route("/api/employees/<int:employee_id>", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_employee(employee_id):
    employee = employee_service.get_by_id(employee_id)
    if employee is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(employee.to_dict()), 200


@employee_controller.route("/api/employees", methods=["POST"])
@token_required
@role_required("HR_ADMIN")
def create_employee():
    data = request.get_json() or {}
    employee = employee_service.create(data)
    return jsonify(employee.to_dict()), 201


@employee_controller.route("/api/employees/<int:employee_id>", methods=["PATCH"])
@token_required
@role_required("HR_ADMIN")
def update_employee(employee_id):
    employee = employee_service.get_by_id(employee_id)
    if employee is None:
        return jsonify({"error": "not found"}), 404

    data = request.get_json() or {}
    employee = employee_service.update(employee_id, data)
    return jsonify(employee.to_dict()), 200


@employee_controller.route("/api/employees/<int:employee_id>", methods=["DELETE"])
@token_required
@role_required("HR_ADMIN")
def delete_employee(employee_id):
    employee = employee_service.get_by_id(employee_id)
    if employee is None:
        return jsonify({"error": "not found"}), 404

    employee_service.delete(employee_id)
    return "", 204


@employee_controller.route("/api/profile", methods=["GET"])
@token_required
@role_required("EMPLOYEE")
def get_my_profile():
    employee = employee_service.get_by_user_id(request.user_id)
    if employee is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(employee.to_dict()), 200