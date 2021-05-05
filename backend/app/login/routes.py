from . import loginBP
# from app.data import todoDB
from flask_json import json_response


@loginBP.route("/admin/", methods=["GET"])
def login():
    return json_response(
        response="Hi Admin", headers={"Content-Type": "application/json"}
    )
