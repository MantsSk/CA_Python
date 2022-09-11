from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
import app

def vaikas_query():
    return app.Vaikas.query

class TevasForm(FlaskForm):
    vardas = StringField('Numeris', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    vaikas = QuerySelectField(query_factory=vaikas_query, allow_blank=True, get_label="vardas", get_pk=lambda obj: str(obj))
    submit = SubmitField('Įvesti')


class VaikasForm(FlaskForm):
    vardas = StringField('Numeris', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    submit = SubmitField('Įvesti')
