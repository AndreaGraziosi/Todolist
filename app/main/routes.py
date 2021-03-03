from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Class, Todo, User
from app.main.forms import ClassForm, TodoForm
from app import bcrypt


from app import app, db

main = Blueprint('main', __name__)

# Create your routes here.
@main.route('/')
def home():
    '''Homepage with handy links'''
    return """
    <html>
    """

@main.route('/add_todo', methods=['POST'])
def add_todo():
    '''add a todo for your class'''
    return """

    HTML

    """
@main.route('/display_todo_list', methods=['GET'])
def display_todo_list():
    """displays todolists for all classes in one place!"""
    return """
    html display_todo_list
    """

@main.route('/delete_list_item', methods=['POST'])
def delete_list_item():
    """deletes list items that have been finished"""

    return """

    delete todo

    """
@main.route('/create_class', methods=['POST'])
def create_class():
    """ creates current classes"""
    return """
        <html>
   """
