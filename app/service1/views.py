from flask import Blueprint
from .subservice1 import *

service1_section = Blueprint('service1_section', __name__)

#Hello Section
@service1_section.route("/")
def helloservice1():
    return ("Welcome to service1!")
