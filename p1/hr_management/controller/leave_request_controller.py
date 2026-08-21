from flask import Blueprint, jsonify, request

from dao.employee_dao import EmployeeDAO
from dao.leave_requests_dao import LeaveRequestDAO
from dao.leave_balance_dao import LeaveBalanceDAO
from dao.leave_types_dao import LeaveTypeDAO
from service.authorization import role_required, token_required
from service.leave_request_service import LeaveRequestService

leave_request_controller = Blueprint("leave_request_controller", __name__)

leave_request_service = LeaveRequestService(
    LeaveRequestDAO(),
    EmployeeDAO(),
    LeaveTypeDAO(),
    LeaveBalanceDAO()
)


@leave_request_controller.route("/api/leave-requests", methods=["POST"])
@token_required
@role_required("EMPLOYEE")
def apply_leave():
    data = request.get_json() or {}

    try:
        leave_request = leave_request_service.apply_leave(
            request.user_id,
            data
        )
        return jsonify({
            "message": "Leave request submitted",
            "leave_request": leave_request.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({
            "error": "Failed to submit leave request",
            "details": str(e)
        }), 500


@leave_request_controller.route("/api/leave-requests", methods=["GET"])
@token_required
@role_required("EMPLOYEE")
def get_my_leave_requests():
    try:
        requests = leave_request_service.get_my_requests(request.user_id)
        return jsonify([leave_request.to_dict() for leave_request in requests]), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({
            "error": "Failed to fetch leave requests",
            "details": str(e)
        }), 500

@leave_request_controller.route(
    "/api/leave-requests/<int:request_id>/approve",
    methods=["PATCH"]
)
@token_required
@role_required("MANAGER", "HR_ADMIN")
def approve_leave(request_id):
    try:
        leave_request = leave_request_service.approve_leave(request_id, request.user_id)
        return jsonify({
            "message": "Leave request approved",
            "leave_request": leave_request.to_dict()
        }), 200
    except ValueError as e:
        status_code = 404 if "not found" in str(e).lower() else 400
        return jsonify({"error": str(e)}), status_code
    except Exception as e:
        return jsonify({
            "error": "Failed to approve leave request",
            "details": str(e)
        }), 500


@leave_request_controller.route(
    "/api/leave-requests/<int:request_id>/reject",
    methods=["PATCH"]
)
@token_required
@role_required("MANAGER", "HR_ADMIN")
def reject_leave(request_id):
    try:
        leave_request = leave_request_service.reject_leave(request_id, request.user_id)
        return jsonify({
            "message": "Leave request rejected",
            "leave_request": leave_request.to_dict()
        }), 200
    except ValueError as e:
        status_code = 404 if "not found" in str(e).lower() else 400
        return jsonify({"error": str(e)}), status_code
    except Exception as e:
        return jsonify({
            "error": "Failed to reject leave request",
            "details": str(e)
        }), 500