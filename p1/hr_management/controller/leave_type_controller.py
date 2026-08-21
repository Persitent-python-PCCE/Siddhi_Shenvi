from flask import Blueprint, jsonify, request

from dao.leave_types_dao import LeaveTypeDAO
from service.authorization import role_required, token_required
from service.leave_type_service import LeaveTypeService

leave_type_controller = Blueprint("leave_type_controller", __name__)
leave_type_service = LeaveTypeService(LeaveTypeDAO())

@leave_type_controller.route("/api/leave-types", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_leave_types():
    leave_types = leave_type_service.get_all()
    return jsonify([leave_type.to_dict() for leave_type in leave_types]), 200

@leave_type_controller.route("/api/leave-types/<int:leave_type_id>", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_leave_type(leave_type_id):
    try:
        leave_type = leave_type_service.get_by_id(leave_type_id)
        return jsonify({"leave_type": leave_type.to_dict()}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@leave_type_controller.route("/api/leave-types", methods=["POST"])
@token_required
@role_required("HR_ADMIN")
def create_leave_type():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    try:
        leave_type = leave_type_service.create_leave_type(data)
        return jsonify({
            "message": "Leave type created successfully",
            "leave_type": leave_type.to_dict()
        }), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Leave type creation failed", "details": str(e)}), 500

@leave_type_controller.route("/api/leave-types/<int:leave_type_id>", methods=["PUT"])
@token_required
@role_required("HR_ADMIN")
def update_leave_type(leave_type_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    try:
        leave_type = leave_type_service.update_leave_type(leave_type_id, data)
        return jsonify({
            "message": "Leave type updated successfully",
            "leave_type": leave_type.to_dict()
        }), 200
    except ValueError as e:
        status_code = 404 if "not found" in str(e).lower() else 400
        return jsonify({"error": str(e)}), status_code
    except Exception as e:
        return jsonify({"error": "Leave type update failed", "details": str(e)}), 500

@leave_type_controller.route("/api/leave-types/<int:leave_type_id>", methods=["DELETE"])
@token_required
@role_required("HR_ADMIN")
def delete_leave_type(leave_type_id):
    try:
        leave_type_service.delete_leave_type(leave_type_id)
        return jsonify({"message": "Leave type deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "Leave type deletion failed", "details": str(e)}), 500