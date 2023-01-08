from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactsForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField(
        'Email', [Email(), DataRequired()])
    content = TextAreaField(
        'Content', [DataRequired(), Length(min=10, message=('Text is too short'))])
    submit = SubmitField('Submit')
