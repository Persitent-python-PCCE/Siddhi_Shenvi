from flask import Blueprint, request, jsonify, render_template

from dao.user_dao import UserDAO
from dao.employee_dao import EmployeeDAO
from service.auth_service import AuthService
from service.authorization import token_required

auth_controller = Blueprint("auth_controller", __name__)
auth_service = AuthService(UserDAO(), EmployeeDAO())

@auth_controller.route("/register", methods=["GET"])
def registration_page():
    return render_template("register.html")

@auth_controller.route("/api/register", methods=["POST"])
def register():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
    try:
        employee = auth_service.register(data)
        return jsonify({
            "message": "User registered successfully",
            "user": employee.to_dict()
        }), 201
    #email already registered error
    except ValueError as e:
         return jsonify({
            "error": str(e)
        }), 400
    #for unexpected errors
    except Exception as e:
        return jsonify({
            "error": "Registration failed",
            "details": str(e)
        }), 500

@auth_controller.route("/api/login", methods=["POST"])
def login():
    data =request.get_json()
    email = data["email"]
    password = data["password"]
    try:
        token = auth_service.login(email, password)
        return jsonify({
        "message": "Login successful",
        "token" : token
        }), 200

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

@auth_controller.route("/api/test", methods=["GET"])
@token_required
def test():

    return jsonify({
        "message": "Token is valid"
    }), 200

