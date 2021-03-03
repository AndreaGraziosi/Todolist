from app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin


class User(UserMixin,db.Model):
    """user model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(200), nullable=False)
    classes = db.relationship('Class', back_populates='users')

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    users = db.relationship('User', back_populates='classes')
    todos = db.relationship('TodoItem', back_populates='todo_for_class')


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    todo_for_class = db.relationship('Class', back_populates='todos')