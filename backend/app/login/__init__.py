from flask import Blueprint

loginBP = Blueprint("login", __name__)
from . import routes

