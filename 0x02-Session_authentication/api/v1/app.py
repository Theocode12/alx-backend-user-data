#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

AuthType = getenv("AUTH_TYPE")
if AuthType == "auth":
    from api.v1.auth.auth import Auth

    auth = Auth()
elif AuthType == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth

    auth = BasicAuth()
elif AuthType == "session_auth":
    from api.v1.auth.session_auth import SessionAuth

    auth = SessionAuth()
elif AuthType == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth

    auth = SessionExpAuth()
elif AuthType == "session_db_auth":
    from api.v1.auth.session_db_auth import SessionDBAuth

    auth = SessionDBAuth()
else:
    auth = None


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


@app.before_request
def authorize():
    """authorize a request"""
    if auth:
        excluded_path = [
            "/api/v1/status/",
            "/api/v1/unauthorized/",
            "/api/v1/forbidden/",
            "/api/v1/auth_session/login/",
        ]
        if auth.require_auth(request.path, excluded_path):
            if not (
                auth.authorization_header(request)
                or auth.session_cookie(request)
            ):
                abort(401)
            if not auth.current_user(request):
                abort(403)
            request.current_user = auth.current_user(request)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
