First: Install the required packages
Make sure you have Python installed on your system. Additionally, you will need to install Flask and Flask-SQLAlchemy. You can use pip for this:


pip install Flask
pip install Flask-SQLAlchemy
Second: Setting up the PostgreSQL database
Before running the application, you need to set up a PostgreSQL database with the necessary credentials (username, password, and database name). Ensure you have PostgreSQL installed on your system.

Create a database named "neo" (or any other name you prefer) and a user "postgres" with the password "jawadibrahim10" (or modify it according to your preferences).

The Flask development server will start, and you should see output indicating that the application is running on http://localhost:5000/.

Third: Test the Application
You can now test the application by sending requests to the defined API endpoints using a tool like  Postman. For example:
open terminal and run
To get all tasks: GET http://localhost:5000/tasks
To create a new task: POST http://localhost:5000/tasks with JSON payload containing the task details.
To update a task: PUT http://localhost:5000/tasks/<task_id> with JSON payload containing the updated task details.
To delete a task: DELETE http://localhost:5000/tasks/<task_id>
and replace <task_id> with the actual task ID when making requests for specific tasks
The application will be accessible at: http://localhost:5000/


