from flask import request, jsonify

from app.data import todoDB
from . import admin_bp


@admin_bp.route("/priority/add/", methods=["POST"])
def priorityAdd():
    response = todoDB.priorityAdd(
        request.get_json()["priorityName"]
    )
    return jsonify(response)


@admin_bp.route("/priority/retrieve/", methods=["GET"])
def priorityRetrieve():
    response = todoDB.priorityRetrieve(
        request.get_json()["priorityId"]
    )
    return jsonify(response)


@admin_bp.route("/status/add/", methods=["POST"])
def statusAdd():
    response = todoDB.statusAdd(
        request.get_json()["statusName"]
    )
    return jsonify(response)


@admin_bp.route("/status/retrieve/", methods=["GET"])
def statusRetrieve():
    response = todoDB.statusRetrieve(
        request.get_json()["statusId"]
    )
    return jsonify(response)


@admin_bp.route("/tag/add/", methods=["POST"])
def tagAdd():
    response = todoDB.tagAdd(
        request.get_json()["tagName"]
    )
    return jsonify(response)


@admin_bp.route("/tag/retrieve/", methods=["GET"])
def tagRetrieve():
    response = todoDB.tagRetrieve(
        request.get_json()["tagId"]
    )
    return jsonify(response)


@admin_bp.route("/tasktype/add/", methods=["POST"])
def taskTypeAdd():
    response = todoDB.taskTypeAdd(
        request.get_json()["taskTypeName"]
    )
    return jsonify(response)


@admin_bp.route("/tasktype/retrieve/", methods=["GET"])
def taskTypeRetrieve():
    response = todoDB.taskTypeRetrieve(
        request.get_json()["taskTypeId"]
    )
    return jsonify(response)
