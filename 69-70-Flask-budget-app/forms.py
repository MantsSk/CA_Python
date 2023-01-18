from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField, FloatField
from wtforms.validators import DataRequired, ValidationError, EqualTo
import app


class RegisterForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField("Repeat password", [
        EqualTo('password', 'Passwords must match')])
    submit = SubmitField('Register')

    def validate_name(self, name):
        with app.app.app_context():
            user = app.User.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError(
                    'This name is in use. Choose another one')

    def validate_email(self, email):
        with app.app.app_context():
            user = app.User.query.filter_by(
                email=email.data).first()
            if user:
                raise ValidationError(
                    'This email is in use. Choose another one.')


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class EntryForm(FlaskForm):
    income = BooleanField('Income')
    sum = FloatField('Sum', [DataRequired()])
    submit = SubmitField('Submit')
