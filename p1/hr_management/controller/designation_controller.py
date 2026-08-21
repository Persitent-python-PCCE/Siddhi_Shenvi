from flask import Blueprint, jsonify, request

from dao.designation_dao import DesignationDAO
from service.authorization import role_required, token_required
from service.designation_service import DesignationService

designation_controller = Blueprint("designation_controller", __name__)
designation_service = DesignationService(DesignationDAO())


@designation_controller.route("/api/designations", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_designations():
    designations = designation_service.get_all()
    return jsonify([designation.to_dict() for designation in designations]), 200

@designation_controller.route("/api/designations/<int:designation_id>", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_designation(designation_id):
    try:
        designation = designation_service.get_by_id(designation_id)
        return jsonify({"designation": designation.to_dict()}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@designation_controller.route("/api/designations", methods=["POST"])
@token_required
@role_required("HR_ADMIN")
def create_designation():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    try:
        designation = designation_service.create_designation(data)
        return jsonify({
            "message": "Designation created successfully",
            "designation": designation.to_dict()
        }), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field: {e.args[0]}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Designation creation failed", "details": str(e)}), 500

@designation_controller.route("/api/designations/<int:designation_id>", methods=["PUT"])
@token_required
@role_required("HR_ADMIN")
def update_designation(designation_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    try:
        designation = designation_service.update_designation(designation_id, data)
        return jsonify({
            "message": "Designation updated successfully",
            "designation": designation.to_dict()
        }), 200
    except ValueError as e:
        status_code = 404 if "not found" in str(e).lower() else 400
        return jsonify({"error": str(e)}), status_code
    except Exception as e:
        return jsonify({"error": "Designation update failed", "details": str(e)}), 500

@designation_controller.route("/api/designations/<int:designation_id>", methods=["DELETE"])
@token_required
@role_required("HR_ADMIN")
def delete_designation(designation_id):
    try:
        designation_service.delete_designation(designation_id)
        return jsonify({"message": "Designation deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "Designation deletion failed", "details": str(e)}), 500