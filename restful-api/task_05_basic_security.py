""""""

# IMPORTS
from flask import Flask, jsonify, request, make_response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "dw03eOgKLyhPmFlkpy8LvmT0WUFF1fFA"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username: str, password: str):
    """"""
    user = users.get(username, None)
    if user is not None and check_password_hash(
        user.get("password", ""), password
    ):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def protected_route() -> str:
    """"""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """"""
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username, None)
    if user is None or not check_password_hash(
        user.get("password", ""), password
    ):
        return jsonify({"ERR": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """"""
    user = get_jwt_identity()
    if users[user].get("role") == "admin":
        return "Admin Access: Granted"
    return make_response(jsonify({"error": "Admin access required"}), 403)


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
