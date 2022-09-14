from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
import app



class ZmogusForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    asmens_kodas = StringField('Asmens kodas', [DataRequired()])
    tel_numeris = StringField('Telefono numeris', [DataRequired()])
    submit = SubmitField('Įvesti žmogų')

class BankasForm(FlaskForm):
    pavadinimas = StringField('Pavadinimas', [DataRequired()])
    adresas = StringField('Adresas', [DataRequired()])
    banko_kodas = StringField('Banko kodas', [DataRequired()])
    swift = StringField('SWIFT kodas', [DataRequired()])
    submit = SubmitField('Įvesti banką')

def zmogus_query():
    return app.Zmogus.query

def bankas_query():
    return app.Bankas.query

class SaskaitaForm(FlaskForm):
    numeris = StringField('Pavadinimas', [DataRequired()])
    zmogus = QuerySelectField("Vartotojas", query_factory=zmogus_query, allow_blank=True, get_label="vardas")
    bankas = QuerySelectField("Bankas", query_factory=bankas_query, allow_blank=True, get_label="pavadinimas")
    balansas = FloatField('Balansas', [DataRequired()])
    submit = SubmitField('Įvesti sąskaitą')






