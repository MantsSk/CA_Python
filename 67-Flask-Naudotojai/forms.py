from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField, TextAreaField, EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo
import app 

class RegistracijosForma(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    el_pastas = EmailField("El.pastas", [DataRequired()]) 
    slaptazodis = PasswordField("Slaptazodis", [DataRequired()])
    patvirtintas_slaptazodis = PasswordField("Pakartokite slaptazodi", [EqualTo('slaptazodis', "Slaptazodis turi but toks pats")])
    submit = SubmitField("Prisiregistruoti")

    def validate_vardas(self, vardas):
        with app.app.app_context():
            vartotojas = app.Vartotojas.query.filter_by(vardas=vardas.data).first()
            if vartotojas:
                raise ValidationError("Sis vardas jau yra musu duomenu bazeje")

    def validate_el_pastas(self, el_pastas):
        with app.app.app_context():
            vartotojas = app.Vartotojas.query.filter_by(el_pastas=el_pastas.data).first()
            if vartotojas:
                raise ValidationError("Sis vardas jau yra musu duomenu bazeje")


class PrisijungimoForma(FlaskForm):
    el_pastas = EmailField("El.pastas", [DataRequired()]) 
    slaptazodis = PasswordField("Slaptazodis", [DataRequired()])
    prisiminti = BooleanField("Prisiminti mane")
    submit = SubmitField("Prisijungti")

class IrasasForm(FlaskForm):
    irasas = TextAreaField('Irasas', [DataRequired()])
    submit = SubmitField('Prideti irasa')