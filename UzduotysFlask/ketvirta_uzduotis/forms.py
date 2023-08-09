from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app import app, Departamentas


def departamentas_query():
    with app.app_context():
        return Departamentas.query.all()


class DarbuotojasForm(FlaskForm):
    vardas = StringField('Vardas', validators=[DataRequired()])
    pavarde = StringField('Pavarde', validators=[DataRequired()])
    departamentas = QuerySelectField(
        query_factory=departamentas_query, get_label='pavadinimas')
    submit = SubmitField('Patvirtinti')


class DepartamentasForm(FlaskForm):
    pavadinimas = StringField('Pavadinimas', validators=[DataRequired()])
    submit = SubmitField('Patvirtinti')
