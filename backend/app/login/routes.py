from . import loginBP
from app.data import todoDB
from flask_json import json_response


@loginBP.route("/login/", methods=["GET"])
def login():
    response = 'Login'
    return json_response(
        response=response, headers={"Content-Type": "application/json"}
    )
