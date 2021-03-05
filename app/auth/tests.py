import os
from unittest import TestCase

from datetime import date
 
from books_app import app, db, bcrypt
from books_app.models import User, Todo, C

"""
Run these tests with the command:
python -m unittest books_app.auth.tests
"""

#################################################
# Setup
#################################################

def add_todo():
    a1 = Course(title='Drafting')
    b1 = Todo(
        description='start blueprints',
        course=a1
    )
    db.session.add(b1)

    a2 = Author(name='Sylvia Plath')
    b2 = Book(title='The Bell Jar', author=a2)
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

class AuthTests(TestCase):
    """Tests for authentication (login & signup)."""

    def setUp(self):
        """Executed prior to each test."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
    
    
    def test_signup(self):
        #  Write a test for the signup route. It should:
        # - Make a POST request to /signup, sending a username & password
        # - Check that the user now exists in the database
        
        post_data = {
            'username' :'me1',
            'password' :'password_hash'
        }
        self.app.post('/signup', data=post_data)

        created_user = User.query.filter_by(username='me1').one()
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user.username,"me1")


    def test_signup_existing_user(self):
        # Write a test for the signup route. It should:
        # - Create a user
        # - Make a POST request to /signup, sending the same username & password
        # - Check that the form is displayed again with an error message
        create_user()

        post_data = {
            'username' :'me1',
            'password' :'password_hash'
        }
        
        res = self.app.post('/signup', data=post_data)
        self.assertEqual(res.status_code,200)
        
        result_page_text = res.get_data(as_text=True)
        self.assertIn('That username is taken. Please choose a different one', result_page_text)


    def test_login_correct_password(self):
        #  Write a test for the login route. It should:
        # - Create a user
        # - Make a POST request to /login, sending the created username & password
        # - Check that the "login" button is not displayed on the homepage
        create_user()
        post_data = {
            'username' :'me1',
            'password' :'password_hash'
        }
        res = self.app.post('/login', data=post_data)
        self.assertEqual(res.status_code, 200)

        result_page_text = res.get_data(as_text=True)
        self.assertNotIn('Login',result_page_text)

    def test_login_nonexistent_user(self):
        # - Write a test for the login route. It should:
        # - Make a POST request to /login, sending a username & password
        # - Check that the login form is displayed again, with an appropriate
        #   error message
        create_user()

        post_data = {
            'username' :'me1',
            'password' :'password_hash'
        }
        res = self.app.post('/signup', data=post_data)
        self.assertEqual(res.status_code, 200)

    def test_login_incorrect_password(self):
        # - Write a test for the login route. It should:
        # - Create a user
        # - Make a POST request to /login, sending the created username &
        #   an incorrect password
        # - Check that the login form is displayed again, with an appropriate
        #   error message
        create_user()
        
        post_data = {
            'username' :'me1',
            'password' :'password_hash_incorrect'
        }
        res = self.app.post('/login', data=post_data)

        result_page_text = res.get_data(as_text=True)
        self.assertNotIn("Password doesn't match. Please try again.", result_page_text)

    def test_logout(self):
        # - Write a test for the logout route. It should:
        # - Create a user
        # - Log the user in (make a POST request to /login)
        # - Make a GET request to /logout
        # - Check that the "login" button appears on the homepage
        create_user()
        post_data = {
            'username' :'me1',
            'password' :'password_hash'
        }
        self.app.post('/login', data=post_data)

        response = self.app.get('/logout', follow_redirects=True)
        response_text = response.get_data(as_text=True)
        self.assertIn('login', response_text)

        