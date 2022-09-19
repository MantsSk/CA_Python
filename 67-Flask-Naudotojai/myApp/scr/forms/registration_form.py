from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from models.User import User


class RegistrationForm(FlaskForm):
    username = StringField('Naudotojas', [DataRequired()])
    email = StringField('El. pastas', [DataRequired()])
    password = PasswordField('Slaptazodis', [DataRequired()])
    verified_password = PasswordField("Pakartokite slaptažodį", [EqualTo('password', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Prisiregistruoti')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Šis naudotojo vardas jau uzimtas. Pasirinkite kitą.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Šis el. pašto adresas uzimtas. Pasirinkite kitą.')


class PrisijungimoForma(FlaskForm):
    email = StringField('El. paštas', [DataRequired()])
    password = PasswordField('Slaptažodis', [DataRequired()])
    remember_me = BooleanField("Prisiminti mane")
    submit = SubmitField('Prisijungti')
