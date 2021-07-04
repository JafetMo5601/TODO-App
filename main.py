from flask import jsonify
from app import app

import todoDB
import os


@app.route("/")
def home():
    return "Hello World!"


@app.route("/api/priority/add/", methods=["POST"])
def priorityAdd():
    response = todoDB.priorityAdd(request.get_json()["priorityName"])
    return jsonify(response)


@app.route("/api/priority/retrieve/", methods=["GET"])
def priorityRetrieve():
    response = todoDB.priorityRetrieve(request.get_json()["priorityId"])
    return jsonify(response)


@app.route("/api/status/add/", methods=["POST"])
def statusAdd():
    response = todoDB.statusAdd(request.get_json()["statusName"])
    return jsonify(response)


@app.route("/api/status/retrieve/", methods=["GET"])
def statusRetrieve():
    response = todoDB.statusRetrieve(request.get_json()["statusId"])
    return jsonify(response)


@app.route("/api/tag/add/", methods=["POST"])
def tagAdd():
    response = todoDB.tagAdd(request.get_json()["tagName"])
    return jsonify(response)


@app.route("/api/tag/retrieve/", methods=["GET"])
def tagRetrieve():
    response = todoDB.tagRetrieve(request.get_json()["tagId"])
    return jsonify(response)


@app.route("/api/tasktype/add/", methods=["POST"])
def taskTypeAdd():
    response = todoDB.taskTypeAdd(request.get_json()["taskTypeName"])
    return jsonify(response)


@app.route("/api/tasktype/retrieve/", methods=["GET"])
def taskTypeRetrieve():
    response = todoDB.taskTypeRetrieve(request.get_json()["taskTypeId"])
    return jsonify(response)


@app.route("/api/tasks/add/", methods=["POST"])
def taskAdd():
    response = todoDB.taskAdd(
        request.get_json()["taskDescription"],
        request.get_json()["taskTypeId"],
        request.get_json()["statusId"],
        request.get_json()["priorityId"],
        request.get_json()["tagId"],
    )

    return jsonify(response, 200)


@app.route("/api/tasks/edit/", methods=["POST"])
def taskEdit():
    response = todoDB.taskEdit(
        request.get_json()["taskId"], request.get_json()["taskDescription"]
    )
    return jsonify(response)


@app.route("/api/tasks/retrieve/", methods=["GET"])
def taskRetrieve():
    response = todoDB.taskRetrieve(request.get_json()["taskId"])
    return jsonify(response)


@app.route("/api/tasks/list/", methods=["GET"])
def taskList():
    response = todoDB.entireTasksRetrieve()
    return jsonify(response)


@app.route("/api/tasks/change/priority/", methods=["POST"])
def taskChangePriority():
    response = todoDB.changeTaskPriority(
        request.get_json()["taskId"], request.get_json()["priorityId"]
    )
    return jsonify(response)


@app.route("/api/tasks/change/status/", methods=["POST"])
def taskChangeStatus():
    response = todoDB.changeTaskStatus(
        request.get_json()["taskId"], request.get_json()["statusId"]
    )
    return jsonify(response)


@app.route("/api/tasks/change/tag/", methods=["POST"])
def taskChangeTag():
    response = todoDB.changeTaskTag(
        request.get_json()["taskId"], request.get_json()["tagId"]
    )
    return jsonify(response)


if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=os.getenv('DEBUG') == 'True')
