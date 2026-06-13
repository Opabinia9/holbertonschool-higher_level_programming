#!/usr/bin/python3
"""M."""

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

database = {"users": {}}


@app.route("/")
def home() -> str:
    """"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data() -> str:
    """"""
    users = database["users"]
    return jsonify(list(users.keys()))


@app.route("/status")
def status() -> str:
    """"""
    return "OK"


@app.route("/users/<username>")
def users(username: str) -> str:
    """"""
    users = database["users"]
    if username not in users:
        return make_response(jsonify({"error": "User not found"}), 404)
    return make_response(jsonify(users[username]), 200)


@app.route("/add_user", methods=["POST"])
def add_user() -> str:
    """"""
    if not request.is_json:
        return make_response(jsonify({"error": "Invalid JSON"}), 400)

    data = request.json
    users = database["users"]
    primary_key = "username"
    user_fields = ["username", "name", "age", "city"]

    if primary_key not in data:
        return make_response(jsonify({"error": "Username is required"}), 400)

    username = data[primary_key]

    if username in users:
        return make_response(
            jsonify({"error": "Username already exists"}), 409
        )
    users[username] = data
    return make_response(
        jsonify({"message": "User Added", username: users[username]}), 201
    )


"""
Return a confirmation message with the added user's data.
"""

if __name__ == "__main__":
    app.run()
