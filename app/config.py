# Config for Flask
# For interactive debugging of Flask apps on Heroku see
# http://stackoverflow.com/a/13946679/64904
DEBUG = True

# Secret for encrypting session cookie content
# Use any random string of characters
SECRET_KEY = "{SESSION_SECRET}"

CONFIG = {
    "_comment"   : "enviroment disponibles: development, testing, production",
    "hostIP"     : "",
    "enviroment" : "development",
    "_puertoProd": "",
    "puertoDev"  : "",
    "_puertoTest": ""
}

DB_CONFIG = {
    "_comment": "Database access",
    "hostIP"  : "",
    "user"    : "",
    "password": "",
    "account" : ""
}