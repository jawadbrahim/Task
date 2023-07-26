
# Import necessary libraries
from flask import Flask,jsonify
from controller import add_get_tasks, update_tasks, get_tasks, delete_tasks
from model import db
from DATABASE import DATABASE_URI 
from marshmallow import ValidationError
# Create a Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
# The DATABASE_URI is imported from the config  and contains the database connection information
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the SQLAlchemy database with the Flask app
db.init_app(app)

# Create all database tables using SQLAlchemy's create_all() method
with app.app_context():
    db.create_all()

# Register the routes with the app object
# Each route is associated with its corresponding handler function from the 'routes' module
# The 'add_get_tasks', 'update_task', 'get_task', and 'delete_task' functions are the handlers for the respective routes
app.route("/tasks", methods=["GET", "POST"])(add_get_tasks)
app.route("/tasks/<int:task_id>", methods=["PUT"])(update_tasks)
app.route("/tasks/<int:task_id>", methods=["GET"])(get_tasks)
app.route("/tasks/<int:task_id>", methods=["DELETE"])(delete_tasks)


# Error handling for Marshmallow validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400
# Run the application 
if __name__ == '__main__':
    app.run(debug=True)
