from app.build.config import Connections
from flask import Flask
from flask_mysqldb import MySQL
from flask_json import FlaskJSON
from flask_cors import CORS, cross_origin

import os


mysql = MySQL()
__connections = Connections()


def createApp():
    app = Flask(__name__)
    CORS(app)
    FlaskJSON(app)
    mysql = __connections.dbConfig(app)
    
    return registerBP(app)


def registerBP(app):
    # Pending to add the registration of the endpoints
    from .login import loginBP
    app.register_blueprint(loginBP)

    from .tasks_management import tasksBP
    app.register_blueprint(tasksBP)

    return app

