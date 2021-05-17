from . import tasksBP
from app.data import todoDB
from flask_json import json_response
from flask import request


@tasksBP.route("/tasks/task-add/", methods=["POST"])
def taskAdd():
    response = todoDB.taskAdd(
        request.get_json()["taskDescription"],
        request.get_json()["taskTypeId"],
        request.get_json()["statusId"],
        request.get_json()["priorityId"],
        request.get_json()["tagId"],
    )
    return json_response(
        response=response, headers={"Content-Type": "application/json"}
    )


@tasksBP.route("/tasks/task-edit/", methods=["POST"])
def taskEdit():
    response = todoDB.taskEdit(
        request.get_json()["taskId"], request.get_json()["taskDescription"]
    )
    return json_response(
        response=response, headers={"Content-Type": "application/json"}
    )


@tasksBP.route("/tasks/task-retrieve/", methods=["GET"])
def taskRetrieve():
    response = todoDB.taskRetrieve(request.get_json()["taskId"])
    return json_response(
        response=response, headers={"Content-Type": "application/json"}
    )


@tasksBP.route("/tasks/tasks-list/", methods=["GET"])
def taskList():
    response = todoDB.entireTasksRetrieve()
    return json_response(
        response=response, headers={"Content-Type": "application/json"}
    )
