import jwt

from functools import wraps
from flask import current_app, request, jsonify


def token_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        auth_header = request.headers.get("Authorization", "")

        if not auth_header.startswith("Bearer "):
            return jsonify({
                "error": "missing token"
            }), 401

        token = auth_header.split(" ", 1)[1]

        try:
            payload = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )

            request.user_id = int(payload["sub"])
            request.role = payload["role"]

        except jwt.ExpiredSignatureError:
            return jsonify({
                "error": "token expired"
            }), 401

        except jwt.InvalidTokenError as e:
            return jsonify({
                "error": "invalid token"
            }), 401

        except Exception as e:
            return jsonify({
                "error": "unexpected token error",
                "details": str(e)
            }), 500

        return func(*args, **kwargs)

    return wrapper

def role_required(*allowed_roles):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if request.role not in allowed_roles:
                return jsonify({
                    "error": "Forbidden"
                }), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator