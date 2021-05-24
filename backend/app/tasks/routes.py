from flask import request, jsonify, json

from app.data import todoDB
from . import tasks_bp


@tasks_bp.route("/tasks/add/", methods=["POST"])
def taskAdd():
    response = todoDB.taskAdd(
        request.get_json()["taskDescription"],
        request.get_json()["taskTypeId"],
        request.get_json()["statusId"],
        request.get_json()["priorityId"],
        request.get_json()["tagId"],
    )
    return jsonify(response, 200)


@tasks_bp.route("/tasks/edit/", methods=["POST"])
def taskEdit():
    response = todoDB.taskEdit(
        request.get_json()["taskId"], request.get_json()["taskDescription"]
    )
    return jsonify(response)


@tasks_bp.route("/tasks/retrieve/", methods=["GET"])
def taskRetrieve():
    response = todoDB.taskRetrieve(request.get_json()["taskId"])
    return jsonify(response)


@tasks_bp.route("/tasks/list/", methods=["GET"])
def taskList():
    response = todoDB.entireTasksRetrieve()
    return jsonify(response)


@tasks_bp.route("/tasks/change/priority/", methods=["POST"])
def taskChangePriority():
    response = todoDB.changeTaskPriority(
        request.get_json()["taskId"], request.get_json()["priorityId"]
    )
    return jsonify(response)


@tasks_bp.route("/tasks/change/status/", methods=["POST"])
def taskChangeStatus():
    response = todoDB.changeTaskStatus(
        request.get_json()["taskId"], request.get_json()["statusId"]
    )
    return jsonify(response)


@tasks_bp.route("/tasks/change/tag/", methods=["POST"])
def taskChangeTag():
    response = todoDB.changeTaskTag(
        request.get_json()["taskId"], request.get_json()["tagId"]
    )
    return jsonify(response)