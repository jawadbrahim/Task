
from flask import Flask,request
from controller import add_get_tasks, update_task, get_task, delete_task
from model import db
from main import app
@app.route("/tasks", methods=["POST", "GET"])
def tasks():
    return add_get_tasks()

@app.route("/tasks/<int:task_id>", methods=["PUT", "GET", "DELETE"])
def task(task_id):
    if request.method == "PUT":
        return update_task(task_id)
    elif request.method == "GET":
        return get_task(task_id)
    elif request.method == "DELETE":
        return delete_task(task_id)