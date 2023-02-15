#!/usr/bin/env python3
"""
Flask app
"""

from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Root Endpoint"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_users():
    """Register users"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
