from flask import (
    Blueprint,
    jsonify,
    request,
    send_file
)

from dao.employee_dao import EmployeeDAO
from dao.employee_documents_dao import EmployeeDocumentsDAO
from service.authorization import (
    role_required,
    token_required
)
from service.employee_documents_service import (
    EmployeeDocumentsService
)

employee_documents_controller = Blueprint(
    "employee_documents_controller",
    __name__
)

employee_documents_service = EmployeeDocumentsService(
    EmployeeDocumentsDAO(),
    EmployeeDAO()
)


@employee_documents_controller.route(
    "/api/documents",
    methods=["POST"]
)
@token_required
@role_required("EMPLOYEE")
def upload_document():
    document_type = request.form.get("document_type")
    file = request.files.get("file")

    try:
        document = employee_documents_service.upload_document(
            request.user_id,
            document_type,
            file
        )
        return jsonify({
            "message": "Document uploaded successfully",
            "document": document.to_dict()
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({
            "error": "Failed to upload document",
            "details": str(e)
        }), 500


@employee_documents_controller.route(
    "/api/documents",
    methods=["GET"]
)
@token_required
@role_required("EMPLOYEE")
def get_my_documents():
    try:
        documents = employee_documents_service.get_my_documents(
            request.user_id
        )
        return jsonify([
            document.to_dict()
            for document in documents
        ]), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({
            "error": "Failed to fetch documents",
            "details": str(e)
        }), 500


@employee_documents_controller.route(
    "/api/documents/<int:document_id>",
    methods=["GET"]
)
@token_required
@role_required("EMPLOYEE")
def get_document(document_id):
    try:
        document = employee_documents_service.get_my_document(
            request.user_id,
            document_id
        )
        return send_file(
            document.file_path,
            download_name=document.file_name
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({
            "error": "Failed to retrieve document",
            "details": str(e)
        }), 500


@employee_documents_controller.route(
    "/api/documents/<int:document_id>",
    methods=["DELETE"]
)
@token_required
@role_required("EMPLOYEE")
def delete_document(document_id):
    try:
        employee_documents_service.delete_my_document(
            request.user_id,
            document_id
        )
        return "", 204
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({
            "error": "Failed to delete document",
            "details": str(e)
        }), 500

@employee_documents_controller.route(
    "/api/employees/<int:employee_id>/documents",
    methods=["GET"]
)
@employee_documents_controller.route("/api/employees/<int:employee_id>/documents", methods=["GET"])
@token_required
@role_required("HR_ADMIN")
def get_employee_documents(employee_id):
    try:
        documents = employee_documents_service.get_employee_documents(employee_id)
        return jsonify([document.to_dict() for document in documents]), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "Failed to fetch employee documents", "details": str(e)}), 500