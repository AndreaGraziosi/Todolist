from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import  Todo, Class, User


class ClassForm(FlaskForm):
    """Form to create a class"""
    title = StringField('Class title',
        validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField("Submit")  

class TodoForm(FlaskForm):
    """Form to create a todo"""
    description = TextAreaField('Todo')
    submit = SubmitField('Submit')

