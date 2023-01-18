from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    first_name = StringField('First name', [DataRequired()])
    last_name = StringField('Last name', [DataRequired()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')
