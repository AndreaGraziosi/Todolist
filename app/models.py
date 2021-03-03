from app import db
from sqlalchemy.orm import backref
from flask_login import UserMixin


class User(UserMixin,db.Model):
    """user model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(200), nullable=False)
    classes = db.relationship('Class',secondary='user_class', back_populates='users')

user_class_table = db.Table('user_class',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('class_id', db.Integer, db.ForeignKey('class.id'))
)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    users = db.relationship('User', secondary='user_class', back_populates='classes')
    todos = db.relationship('Todo', secondary='class_todo',back_populates='todo_for_class')

class_todo_table = db.Table('class_todo',
    db.Column('class_id', db.Integer, db.ForeignKey('class.id')),
    db.Column('todo_id', db.Integer, db.ForeignKey('todo.id'))
)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), nullable=False)
    todo_for_class = db.relationship('Class', secondary='class_todo', back_populates='todos')