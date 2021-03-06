# Create your tests here.
import os
import unittest
 
from app import app, db, bcrypt
from app.models import User, Todo, Course

"""
Run these tests with the command:
python -m unittest app.main.tests
"""

#################################################
# Setup
#################################################

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def create_todo():
    a1 = Course(title='Mathematics')
    b1 = Todo(
        description='Finish math homework',
        course=a1
    )
    db.session.add(b1)

    a2 = Course(title='English')
    b2 = Todo(description='write essay', course=a2)
    db.session.add(b2)
    db.session.commit()

def create_user():
    password_hash = bcrypt.generate_password_hash('password').decode('utf-8')
    user = User(username='me1', password=password_hash)
    db.session.add(user)
    db.session.commit()




#################################################
# Tests
#################################################

class MainTests(unittest.TestCase):
 
    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
    def test_homepage_logged_out(self):
        """makes sure that todos show up on homepage"""
        create_todo()
        create_user()

        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response_text = response.get_data(as_text=True)
        self.assertIn('Finish math homework', response_text)
        self.assertIn('write essay', response_text)
        self.assertIn('me1', response_text)
        self.assertIn('Log In', response_text)
        self.assertIn('Sign Up', response_text)

        self.assertNotIn('Add todo', response_text)
        self.assertNotIn('Create a course', response_text)
        


    def add_todo(self):
        """test adding a todo"""
        create_todo()
        create_user()
        login(self.app, 'me1', 'password')

        post_data ={
            "description": "Make Flashcards",
            "todo_for_course": "todo: 1"

        }
        self.app.post('/create_todo', data=post_data)

        created_todo = Todo.query.filter_by(description='Make Flashcards').one()
        self.assertIsNotNone(created_todo)
        self.assertEqual(created_todo.todo_for_course, 1)
    def create_course():
        pass

    def display_todos(course_id):
        pass

    def profile(username):
        pass

    