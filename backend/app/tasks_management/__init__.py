from flask import Blueprint

tasksBP = Blueprint("tasks", __name__)
from . import routes
