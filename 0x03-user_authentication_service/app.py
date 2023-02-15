#!/usr/bin/env python3
"""
Flask app
"""

from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=["POST"])
def login():
    """Login the user"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        resp = jsonify({"email": f"{email}", "message": "logged in"})
        resp.set_cookie("session_id", session_id)
        return resp
    abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """Logs out users by destroying session"""
    session_id = request.cookies.get("session_id")
    user_obj = AUTH.get_user_from_session_id(session_id)
    if user_obj:
        AUTH.destroy_session(user_obj.id)
        return redirect("/", code=302)
    else:
        abort(403)


@app.route("/profile", methods=["GET"])
def profile():
    """Find a user by their session id."""
    session_id = request.cookies.get("session_id")
    user_obj = AUTH.get_user_from_session_id(session_id)
    if user_obj:
        return jsonify({"email": f"{user_obj.email}"})
    abort(403)


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """Sets a reset password token to a user"""
    try:
        email = request.form.get("email")
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": f"{email}", "reset_token": f"{token}"})
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """Update user password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, password)
        return jsonify({"email": f"{email}", "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
