from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, StringField, PasswordField, FloatField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from flask_wtf.file import FileField, FileAllowed
import app


class RegistracijosForma(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    el_pastas = StringField('El. paštas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    patvirtintas_slaptazodis = PasswordField("Pakartokite slaptažodį", [
                                             EqualTo('slaptazodis', "Slaptažodis turi sutapti.")])
    submit = SubmitField('Prisiregistruoti')

    def tikrinti_varda(self, vardas):
        with app.app_context():
            vartotojas = app.Vartotojas.query.filter_by(
                vardas=vardas.data).first()
            if vartotojas:
                raise ValidationError(
                    'Šis vardas panaudotas. Pasirinkite kitą.')

    def tikrinti_pasta(self, el_pastas):
        with app.app_context():
            vartotojas = app.Vartotojas.query.filter_by(
                el_pastas=el_pastas.data).first()
            if vartotojas:
                raise ValidationError(
                    'Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class PrisijungimoForma(FlaskForm):
    el_pastas = StringField('El. paštas', [DataRequired()])
    slaptazodis = PasswordField('Slaptažodis', [DataRequired()])
    prisiminti = BooleanField("Prisiminti mane")
    submit = SubmitField('Prisijungti')


class IrasasForm(FlaskForm):
    pajamos = BooleanField('Pajamos')
    suma = FloatField('Suma', [DataRequired()])
    submit = SubmitField('Įvesti')


class PaskyrosAtnaujinimoForma(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    el_pastas = StringField('El. paštas', [DataRequired()])
    nuotrauka = FileField('Atnaujinti profilio nuotrauką',
                          validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Atnaujinti')

    def tikrinti_varda(self, vardas):
        if vardas.data != app.current_user.vardas:
            vartotojas = app.Vartotojas.query.filter_by(
                vardas=vardas.data).first()
            if vartotojas:
                raise ValidationError(
                    'Šis vardas panaudotas. Pasirinkite kitą.')

    def tikrinti_pasta(self, el_pastas):
        if el_pastas.data != app.current_user.el_pastas:
            vartotojas = app.Vartotojas.query.filter_by(
                el_pastas=el_pastas.data).first()
            if vartotojas:
                raise ValidationError(
                    'Šis el. pašto adresas panaudotas. Pasirinkite kitą.')


class UzklausosAtnaujinimoForma(FlaskForm):
    el_pastas = StringField('El. paštas', validators=[DataRequired(), Email()])
    submit = SubmitField('Gauti')

    def validate_email(self, el_pastas):
        user = app.Vartotojas.query.filter_by(el_pastas=el_pastas.data).first()
        if user is None:
            raise ValidationError(
                'Nėra paskyros, registruotos šiuo el. pašto adresu. Registruokitės.')


class SlaptazodzioAtnaujinimoForma(FlaskForm):
    slaptazodis = PasswordField('Slaptažodis', validators=[DataRequired()])
    patvirtintas_slaptazodis = PasswordField('Pakartokite slaptažodį', validators=[
                                             DataRequired(), EqualTo('slaptazodis')])
    submit = SubmitField('Atnaujinti Slaptažodį')
