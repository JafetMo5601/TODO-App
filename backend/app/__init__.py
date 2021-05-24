from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
# from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
import os

from instance.config import app_config


# login_manager = LoginManager()
mysql = MySQL()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app = config_app(app, config_name)
    # db.init_app(app)
    mysql = MySQL(app)
    CORS(app)

    return app 


def config_app(app, config):
    app.config.from_object(app_config[config])
    app.config.from_pyfile('config.py')    
    app.config["MYSQL_HOST"] = "localhost"
    app.config["MYSQL_USER"] = "root"
    app.config["MYSQL_PASSWORD"] = os.getenv('DBPASSWD')
    app.config["MYSQL_DB"] = "todo"
    app = register_bp(app)

    # login_manager.init_app(app)
    # login_manager.login_message = "You must be logged in to access this page"
    # login_manager.login_view = "auth.login"
    
    return app

def register_bp(app):
    from app.tasks import tasks_bp
    app.register_blueprint(tasks_bp)
    
    from app.admin import admin_bp
    app.register_blueprint(admin_bp)

    return app