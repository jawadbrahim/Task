
from flask import  jsonify, request

from model import Task,db
from schema import TaskSchema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

def add_get_tasks():
     # Handle POST request to add a new task
    if request.method == "POST":
        # Retrieve task information from the JSON data in the request
        tasks_title = request.json["title"]
        tasks_description = request.json.get("description")
        tasks_completed = request.json.get("completed")
         # Create a new Task instance with the provided data
        new_task = Task(tasks_title, tasks_description, tasks_completed)
         # Add the new task to the database session
        db.session.add(new_task)
         # Commit the changes to the database
        db.session.commit()
          # Return a response message "Task created successfully" with a status code 201
        return "Task created successfully", 201
        
# Handle GET request to retrieve all tasks
    tasks_list = Task.query.all()
    tasks = []
     # Convert tasks to a list of dictionaries, where each dictionary represents a task
    for task in tasks_list:
        tasks.append({"title": task.title, "description": task.description, "completed": task.completed})
 # Return a JSON response containing the list of tasks
    return jsonify({"tasks": tasks})

 # Retrieve the task from the database based on the provided task_id
def update_tasks(task_id):
    task = Task.query.get(task_id)
    # Check if the task exists
    if task:
         # Retrieve task information from the JSON data in the request
        tasks_title = request.json["title"]
        tasks_description = request.json.get("description", task.description)  
        tasks_completed = request.json.get("completed", task.completed)  
         # Update the task's attributes with the provided data
        task.title = tasks_title
        task.description = tasks_description
        task.completed = tasks_completed
        db.session.commit()
        return "Task updated successfully", 200

 # Retrieve the task from the database based on the provided task_id
def get_tasks(task_id):
    task = Task.query.get(task_id)
    if task:
         # Return a JSON response containing the task's information (title, description, completed)
        return jsonify({"title": task.title, "description": task.description, "completed": task.completed})


def delete_tasks(task_id):
    task = Task.query.get(task_id)
    if task:
          # Delete the task from the database session
        db.session.delete(task)

        db.session.commit()
        return "Task deleted successfully", 200