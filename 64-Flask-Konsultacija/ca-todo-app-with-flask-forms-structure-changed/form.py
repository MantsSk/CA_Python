from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    name = StringField('Task', [DataRequired()])
    submit = SubmitField('Add task')


class UpdateForm(FlaskForm):
    name = StringField('Task', [DataRequired()])
    submit = SubmitField('Update task')