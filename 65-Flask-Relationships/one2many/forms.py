from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from app import app, Vaikas, Tevas


def query_vaikai():
    with app.app_context():
        return Vaikas.query.all()


def query_tevas():
    with app.app_context():
        return Tevas.query.all()


class TevasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    vaikai = QuerySelectMultipleField(
        query_factory=query_vaikai, get_label="vardas")
    submit = SubmitField('Įvesti')


class VaikasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    tevas = QuerySelectField(query_factory=query_tevas, get_label="vardas")
    submit = SubmitField('Įvesti')
