from flask import Flask,jsonify,request
from urllib.parse import urlparse
from .config import CONFIG

from .views import core
from .service1 import service1_section
from .producer import producer_section

app = Flask(__name__)
app.config.from_pyfile("config.py")

app.register_blueprint(core)

#Register sections blueprints
app.register_blueprint(service1_section,url_prefix='/service1/')
app.register_blueprint(service1.views.subservice1_section,url_prefix='/service1/')

app.register_blueprint(producer_section,url_prefix='/producer/')
#Management of errors

@app.errorhandler(404)
def page_not_found(e):
    toRet = {}
    urlCompleta = urlparse(request.url)
    toRetStr = (str(urlCompleta.path) + " - "+str(e))

    toRet["retVal"]  = "01"
    toRet["retTxt"]  = str(e.code) +": "+str(e.name) +" - "+str(urlCompleta.path)
    toRet["retData"] = {
        "error":str(toRetStr),
        "parseResult":str(urlCompleta)
    }

    return jsonify(toRet)

@app.errorhandler(405)
def page_not_found(e):
    toRet = {}
    urlCompleta = urlparse(request.url)
    toRetStr = (str(urlCompleta.path) + " - "+str(e))

    toRet["retVal"]  = "01"
    toRet["retTxt"]  = str(e.code) +": "+str(e.name) +" - "+str(urlCompleta.path)
    toRet["retData"] = {
        "error":str(toRetStr),
        "parseResult":str(urlCompleta)
    }
    return jsonify(toRet)
