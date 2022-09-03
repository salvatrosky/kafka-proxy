from flask import Blueprint,jsonify
from .controller import function1

subservice1_section = Blueprint('subservice1_section', __name__)

@subservice1_section.route("/subservice1")
def hellosubservice1():
    return ("Welcome to subservice1")

@subservice1_section.route("/subservice1/<page>",methods=['POST'])
def subservice1(page):
    try:
        return function1()
    except:
        return "not ok"
    