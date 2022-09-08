from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired

class IrasasForm(FlaskForm):
    pajamos = BooleanField('Pajamos')
    suma = FloatField('Suma', [DataRequired()])
    submit = SubmitField('Įvesti')
