from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):

    email = StringField('Email', [Email(message=(
        'Incorrect email.')), DataRequired(message='Email is required')])
    password = PasswordField('Password', validators=[Length(min=8, message=(
        'Password should be at least 8 characters')), DataRequired(message='Password is required')])
    address1 = StringField('Address (line 1)', validators=[DataRequired(
        message=('Address is required')), Length(min=4, message=('Address should be at least 4 characters'))])
    address2 = StringField('Address (line 2))', validators=[
                           Length(min=4, message=('Address should be at least 4 characters'))])
    city = StringField('City', validators=[DataRequired(
        message='City is required'), Length(min=4, message=('City should be at least 4 characters'))])
    state = SelectField('State', choices=[('vln', 'Vilniaus'), ('kns', 'Kauno'), (
        'klp', 'Klaipėdos')], validators=[DataRequired(message='State is required')])
    zip_code = StringField('Zip code', validators=[DataRequired(
        message='Zip code is required'), Length(min=4, message=('Zip code should be at least 4 characters'))])
    agree = BooleanField('I agree to get spam')
    submit = SubmitField('Submit')
