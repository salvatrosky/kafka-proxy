from flask import Blueprint,request, make_response,jsonify

from .controller import produce

import logging

producer_section = Blueprint('producer_section', __name__)

#Hello Section
@producer_section.route("/")
def hellosProducer():
    return ("Welcome to Producer!")

@producer_section.route("/produce/<topic>",methods= ["POST"])
def produce_(topic):
    responseData = {}
    try:
        data = request.json
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        responseData["message"] = "Exception occurred obtaining data Session "+str(e)
        responseData["status"] = 2
    
        return (make_response(jsonify(responseData)))

    resultado = produce(topic,data)

    responseData["status"] = 1
    return (make_response(jsonify(responseData)))
