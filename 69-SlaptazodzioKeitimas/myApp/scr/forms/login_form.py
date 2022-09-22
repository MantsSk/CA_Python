from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Slapyvardis', [DataRequired()])
    password = PasswordField('Slaptažodis', [DataRequired()])
    remember_me = BooleanField("Prisiminti mane")
    submit = SubmitField('Prisijungti')
