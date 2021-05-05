from app.build.config import Connections
from flask import Flask
from flask_mysqldb import MySQL
from flask_json import FlaskJSON

import os


mysql = MySQL()
__connections = Connections()


def createApp():
    app = Flask(__name__)
    FlaskJSON(app)
    mysql = __connections.dbConfig(app)
    return registerBP(app)


def registerBP(app):
    # Pending to add the registration of the endpoints
    from .login import loginBP

    app.register_blueprint(loginBP)

    return app

