from flask_mysqldb import MySQL

import os


class Connections:
    def dbConfig(self, app):
        app.config["MYSQL_HOST"] = "localhost"
        app.config["MYSQL_USER"] = "root"
        app.config["MYSQL_PASSWORD"] = os.environ.get("DBPASSWD")
        app.config["MYSQL_DB"] = "todo"
        return MySQL(app)

    def __del__(self):
        print("Destructing connections...")

