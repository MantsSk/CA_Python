from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email


class DarbuotojuForma(FlaskForm):
    vardas = StringField(
        'Vardas', [DataRequired(message='Vardas yra būtinas')])
    pavarde = StringField(
        'Pavardė', [DataRequired(message='Pavardė yra būtina')])
    el_pastas = StringField(
        'El. paštas', [DataRequired(message='El. paštas yra būtinas'), Email(message='El. paštas turi būti validaus formato')])
    tel_numeris = StringField(
        'Telefono numeris', [DataRequired(message='Telefono numeris yra būtinas')])
    alga = DecimalField(
        'Alga', [DataRequired(message='Alga yra būtina')])
    submit = SubmitField('Patvirtinti')
