from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import app

def get_pk(obj):
    return str(obj)

def vaikas_query():
    return app.Vaikas.query

def tevas_query():
    return app.Tevas.query

class TevasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    vaikai = QuerySelectMultipleField(query_factory=vaikas_query, get_label="vardas")
    submit = SubmitField('Įvesti')

class VaikasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    tevas = QuerySelectField(query_factory=tevas_query, get_label="vardas")
    submit = SubmitField('Įvesti')