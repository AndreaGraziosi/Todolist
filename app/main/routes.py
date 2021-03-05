from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Course, Todo, User
from app.main.forms import CourseForm, TodoForm
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

@main.route('/add_todo', methods=['GET','POST']) #for POST request.form.get()
@login_required
def add_todo():
    '''add a todo for your courses'''
    form = TodoForm()

    if form.validate_on_submit():
        new_todo = Todo(
           description = form.description.data,
           todo_for_course = form.todo_for_course.data
        )
        db.session.add(new_todo)
        db.session.commit()

        flash('Great! let\'s get to work!')
        return redirect(url_for('main.display_todos', todo_id=new_todo.id))
    return render_template('add_todo.html', form=form)

@main.route('/create_course', methods=['GET','POST'])
@login_required
def create_course():
    form = CourseForm()
    
    
    if form.validate_on_submit():
        new_course = Course(
           title = form.title.data
        )
    
        db.session.add(new_course)
        db.session.commit()

        flash('Great! What needs to get done for this course?')
        return redirect(url_for('main.homepage', course_id=new_course.id))
    return render_template('create_course.html', form=form)


@main.route('/display_todos/<course_id>', methods=['GET', 'POST'])
@login_required
def display_todos(course_id):
    """displays todolists for all courses in one place!"""
    
    todos = Todo.query.get(course_id)
    form = TodoForm(obj=todos)
    
    if form.validate_on_submit():
        todos.description = form.description.data
    #return a list containg each of the todos  
        db.session.commit()  

        flash('Your todo was updated successfully.')
        return redirect(url_for('main.display_todos', course_id=course_id))
    
    return render_template("display_todos.html", todos=todos,form=form)


@main.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).one()
    return render_template('profile.html', user=user)

@main.route('/delete_list_item <todo_id>', methods=['POST'])
@login_required
def delete_list_item(todo_id):
    """deletes list items that have been finished"""
    todo = Todo.query.get(todo_id)
    if todo not in current_user.todo_for_class:
        flash('this todo was not in the list')
    else:
        current_user.todo_for_course.remove(todo)
        db.session.add(current_user)
        db.session.commit()
        flash('Done with this todo!')
    return redirect(url_for('main.display_todos', todo_id=todo_id))





