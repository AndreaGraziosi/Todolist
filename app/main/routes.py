from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Class, Todo, User
from app.main.forms import ClassForm, TodoForm
from app import bcrypt


from app import app, db

main = Blueprint('main', __name__)

# Create your routes here.

@main.route('/')
def homepage():
    all_todo = Todo.query.all()
    all_users = User.query.all()
    return render_template('homepage.html',
        all_todo=all_todo, all_users=all_users)

@main.route('/add_todo', methods=['POST'])#for POST request.form.get()
def add_todo():
    '''add a todo for your class'''
    return """

    HTML
 # class info so todo goes under the class 

    """

@main.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).one()
    return render_template('profile.html', user=user)


# @main.route('/display_todos', methods=['GET'])
# def get_todos():
#     """displays todolists for all classes in one place!"""
#     class_name = request.args.get('class')
#     #create a database query to retrieve todos linked the class selected

#     #return a list containg each of the todos 
     
#     return render_template("display_todos.html",#return the list )



# @main.route('/delete_list_item', methods=['POST'])
# def delete_list_item():
#     """deletes list items that have been finished"""
#     # error message? if item exists/ suceess messsage 
#     # redirect to main page  
#     return """

#     delete todo

#     """
# @main.route('/create_class', methods=['POST'])
# def create_class():
#     """ creates current classes"""
#     return """
#         <html>
#    """
