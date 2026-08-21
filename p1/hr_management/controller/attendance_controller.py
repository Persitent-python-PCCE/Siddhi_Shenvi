from flask import Blueprint, jsonify, request

from dao.attendance_dao import AttendanceDAO
from dao.employee_dao import EmployeeDAO
from service.attendance_service import AttendanceService
from service.authorization import role_required, token_required

attendance_controller = Blueprint("attendance_controller", __name__)
attendance_service = AttendanceService(AttendanceDAO(), EmployeeDAO())


@attendance_controller.route("/api/attendance/check-in", methods=["POST"])
@token_required
@role_required("EMPLOYEE")
def check_in():
    try:
        attendance = attendance_service.check_in(request.user_id)
        return jsonify({
            "message": "Check-in successful",
            "attendance": attendance.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Check-in failed", "details": str(e)}), 500


@attendance_controller.route("/api/attendance/check-out", methods=["POST"])
@token_required
@role_required("EMPLOYEE")
def check_out():
    try:
        attendance = attendance_service.check_out(request.user_id)
        return jsonify({
            "message": "Check-out successful",
            "attendance": attendance.to_dict()
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Check-out failed", "details": str(e)}), 500


@attendance_controller.route("/api/attendance", methods=["GET"])
@token_required
@role_required("EMPLOYEE")
def get_attendance():
    try:
        attendance = attendance_service.get_my_attendance(request.user_id)
        return jsonify([record.to_dict() for record in attendance]), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404