from app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin


class User(UserMixin,db.Model):
    """user model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(200), nullable=False)
   
    # What courses is this user taking?
    
    courses = db.relationship('Course', back_populates='user')
    

    def __repr__(self):
        return f'User: {self.username}'


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    user = db.relationship('User', back_populates='courses')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # what todos are due for this course?
    todos = db.relationship('Todo',back_populates='todo_for_course')

def __str__(self):
        return f'Course: {self.title}'

def __repr__(self):
        return f'Course: {self.title}'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    todo_for_course = db.relationship('Course', back_populates='todos')

def __str__(self):
    return f'Todo: {self.description}'

def __repr__(self):
    return f'Todo: {self.description}'