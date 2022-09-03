from flask import Flask, request, Blueprint,jsonify
from urllib.parse import urlparse

core = Blueprint("core", __name__)

@core.route("/")
def index():
    return "Welcome!"


