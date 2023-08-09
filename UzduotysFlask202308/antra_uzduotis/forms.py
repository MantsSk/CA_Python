from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class StudentuForma(FlaskForm):
    vardas = StringField(
        'Vardas', [DataRequired(message='Vardas yra būtinas')])
    pavarde = StringField(
        'Pavardė', [DataRequired(message='Pavardė yra būtina')])
    el_pastas = StringField(
        'El. paštas', [DataRequired(message='El. paštas yra būtinas'), Email(message='El. paštas turi būti validaus formato')])
    submit = SubmitField('Patvirtinti')
