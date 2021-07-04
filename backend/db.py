from flask_mysqldb import MySQL
from .app import app

import os


mysql = MySQL()

app.config["MYSQL_HOST"] = os.getenv("DBHOST")
app.config["MYSQL_USER"] = os.getenv("DBUSER")
app.config["MYSQL_PASSWORD"] = os.getenv("DBPASSWD")
app.config["MYSQL_DB"] = os.getenv("DBNAME")

mysql = MySQL(app)
