#!/usr/bin/env python3
"""
This module handles all possible routes for
session authentication.
"""
from flask import abort
from api.v1.views import app_views

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_login():
    """pass"""
    