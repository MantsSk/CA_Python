from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from app import app, Departamentas, Darbuotojas


def departamentas_query():
    with app.app_context():
        return Departamentas.query.all()


def darbuotojas_query():
    with app.app_context():
        return Darbuotojas.query.all()


class DarbuotojasForm(FlaskForm):
    vardas = StringField('Vardas', validators=[DataRequired()])
    pavarde = StringField('Pavarde', validators=[DataRequired()])
    departamentai = QuerySelectField(
        query_factory=departamentas_query, get_label='pavadinimas')
    submit = SubmitField('Patvirtinti')


class DepartamentasForm(FlaskForm):
    pavadinimas = StringField('Pavadinimas', validators=[DataRequired()])
    darbuotojai = QuerySelectMultipleField(
        query_factory=darbuotojas_query, get_label='vardas')
    submit = SubmitField('Patvirtinti')
