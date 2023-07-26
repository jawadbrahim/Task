from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(250))
    description=db.Column(db.String(250))
    completed=db.Column(db.Boolean)
    def __init__(self,title,description,completed):
        self.title=title
        self.description=description
        self.completed=completed
