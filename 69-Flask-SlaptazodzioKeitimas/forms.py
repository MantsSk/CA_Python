from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import (
    SubmitField,
    BooleanField,
    StringField,
    PasswordField,
    TextAreaField,
    EmailField,
)
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
import app
import re


def utility_password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

    # overall result
    password_ok = not (
        length_error
        or digit_error
        or uppercase_error
        or lowercase_error
        or symbol_error
    )

    return password_ok


class RegistracijosForma(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    el_pastas = EmailField("El.pastas", [DataRequired()])
    slaptazodis = PasswordField("Slaptazodis", [DataRequired()])
    patvirtintas_slaptazodis = PasswordField(
        "Pakartokite slaptazodi",
        [EqualTo("slaptazodis", "Slaptazodis turi but toks pats")],
    )
    submit = SubmitField("Prisiregistruoti")

    def validate_vardas(self, vardas):
        with app.app.app_context():
            vartotojas = app.Vartotojas.query.filter_by(vardas=vardas.data).first()
            if vartotojas:
                raise ValidationError("Sis vardas jau yra musu duomenu bazeje")

    def validate_el_pastas(self, el_pastas):
        with app.app.app_context():
            vartotojas = app.Vartotojas.query.filter_by(
                el_pastas=el_pastas.data
            ).first()
            if vartotojas:
                raise ValidationError("Sis vardas jau yra musu duomenu bazeje")

    # def validate_slaptazodis(self, slaptazdodis):
    #     tinkamas_slaptazodis = utility_password_check(slaptazdodis.data)

    #     if not tinkamas_slaptazodis:
    #         raise ValidationError("Slaptazodis netinkamas")


class PaskyrosAtnaujinimoForma(FlaskForm):
    vardas = StringField("Vardas", [DataRequired()])
    el_pastas = EmailField("El.pastas", [DataRequired()])
    nuotrauka = FileField(
        "Atnaujinti profilio nuotrauka",
        validators=[FileAllowed(["jpg", "jpeg", "png"])],
    )
    submit = SubmitField("Atnaujinti")

    def validate_vardas(self, vardas):
        if current_user.vardas != vardas.data:
            with app.app.app_context():
                vartotojas = app.Vartotojas.query.filter_by(vardas=vardas.data).first()
                if vartotojas:
                    raise ValidationError("Sis vardas jau yra musu duomenu bazeje")

    def validate_el_pastas(self, el_pastas):
        if current_user.el_pastas != el_pastas.data:
            with app.app.app_context():
                vartotojas = app.Vartotojas.query.filter_by(
                    el_pastas=el_pastas.data
                ).first()
                if vartotojas:
                    raise ValidationError("Sis el pastas jau yra musu duomenu bazeje")


class PrisijungimoForma(FlaskForm):
    el_pastas = EmailField("El.pastas", [DataRequired()])
    slaptazodis = PasswordField("Slaptazodis", [DataRequired()])
    prisiminti = BooleanField("Prisiminti mane")
    submit = SubmitField("Prisijungti")


class IrasasForm(FlaskForm):
    irasas = TextAreaField("Irasas", [DataRequired()])
    submit = SubmitField("Prideti irasa")

class UzklausosAtnaujinimoForma(FlaskForm):
    el_pastas = EmailField("El. pastas", validators=[DataRequired()])
    submit = SubmitField("Gauti")

    def validate_el_pastas(self, el_pastas):
        with app.app.app_context(): # Ne visai grazu, fix #1
            user = app.Vartotojas.query.filter_by(el_pastas=el_pastas.data).first()
            if user is None:
                raise ValidationError("Nera tokios paskyros")

class SlaptazodzioAtnaujinimoForma(FlaskForm):
    slaptazodis = PasswordField("Slaptazodis", [DataRequired()])
    patvirtintas_slaptazodis = PasswordField(
        "Pakartokite slaptazodi",
        [EqualTo("slaptazodis", "Slaptazodis turi but toks pats")],
    )
    submit = SubmitField("Atnaujinti slaptazodi")
