from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import json
import os


mysql = MySQL()


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path="",
        static_folder="dist",
        template_folder="dist",
    )
    app = config_app(app)
    mysql = MySQL(app)
    CORS(app)

    return app


def config_app(app):
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["MYSQL_HOST"] = os.getenv("DBHOST")
    app.config["MYSQL_USER"] = os.getenv("DBUSER")
    app.config["MYSQL_PASSWORD"] = os.getenv("DBPASSWD")
    app.config["MYSQL_DB"] = os.getenv("DBNAME")
    app = register_bp(app)

    return app


def register_bp(app):
    from app.tasks import tasks_bp

    app.register_blueprint(tasks_bp)

    from app.admin import admin_bp

    app.register_blueprint(admin_bp)

    from app.home import home_bp

    app.register_blueprint(home_bp)

    return app
