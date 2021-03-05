from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from app.models import  Todo, Course, User


class CourseForm(FlaskForm):
    """Form to create a course"""
    title = StringField('course title',
        validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField("Submit")  

class TodoForm(FlaskForm):
    """Form to create a todo"""
    todo_for_course = QuerySelectMultipleField('Courses',
        query_factory=lambda: Course.query)
    description = TextAreaField('Todos')
    submit = SubmitField('Submit')

