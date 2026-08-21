from flask import Blueprint, jsonify, request

from dao.department_dao import DepartmentDAO
from service.authorization import role_required, token_required
from service.department_service import DepartmentService

department_controller = Blueprint("department_controller", __name__)
department_service = DepartmentService(DepartmentDAO())


@department_controller.route("/api/departments", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_departments():
    departments = department_service.get_all()
    return jsonify([department.to_dict() for department in departments]), 200


@department_controller.route("/api/departments/<int:department_id>", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_department(department_id):
    department = department_service.get_by_id(department_id)
    if department is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(department.to_dict()), 200


@department_controller.route("/api/departments", methods=["POST"])
@token_required
@role_required("HR_ADMIN")
def create_department():
    data = request.get_json() or {}
    department = department_service.create(data)
    return jsonify(department.to_dict()), 201


@department_controller.route("/api/departments/<int:department_id>", methods=["PATCH"])
@token_required
@role_required("HR_ADMIN")
def update_department(department_id):
    department = department_service.get_by_id(department_id)
    if department is None:
        return jsonify({"error": "not found"}), 404

    data = request.get_json() or {}
    department = department_service.update(department_id, data)
    return jsonify(department.to_dict()), 200


@department_controller.route("/api/departments/<int:department_id>", methods=["DELETE"])
@token_required
@role_required("HR_ADMIN")
def delete_department(department_id):
    department = department_service.get_by_id(department_id)
    if department is None:
        return jsonify({"error": "not found"}), 404

    department_service.delete(department_id)
    return "", 204