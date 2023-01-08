from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
import app


def query_vaikai():
    with app.app.app_context():  # cia nelabai grazu, bet kolk as palieku ryt sutvarkysiu
        return app.Vaikas.query.all()


class TevasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    vaikas = QuerySelectField(
        query_factory=query_vaikai, allow_blank=True, get_label="vardas")
    submit = SubmitField('Įvesti')


class VaikasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    submit = SubmitField('Įvesti')
