from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from models.User import User

class RequestResetForm(FlaskForm):
    email = StringField('El. paštas', validators=[DataRequired(), Email()])
    submit = SubmitField('Gauti')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Nėra paskyros, registruotos šiuo el. pašto adresu. Registruokitės.')

class PasswordResetForm(FlaskForm):
    password = PasswordField('Slaptažodis', validators=[DataRequired()])
    confirm_password = PasswordField('Pakartokite slaptažodį', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Atnaujinti Slaptažodį')