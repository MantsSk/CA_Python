import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # importuojame migracijas

basedir = os.path.abspath(os.path.dirname(__file__))
# pilnas kelias iki šio failo.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
# nustatėme, kad mūsų duomenų bazė bus šalia šio failo esants data.sqlite failas

db = SQLAlchemy(app)
# sukuriame duomenų bazės objektą
# sukurkime modelį užklausos formai, kuris sukurs duomenų bazėje lentelę

Migrate(app, db)  # Susiejame app ir db.


class Message(db.Model):
    # DB lentelei priskiria pavadinimą, jei nenurodysite, priskirs automatiškai pagal klasės pavadinimą.
    __tablename__ = 'messages'
    # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Papildome duomenų bazės modelį nauju stulpeliu.
    phone = db.Column(db.String(40), unique=True)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message, phone):  # Inbuilt funkcija - Konstruktorius
        self.name = name
        self.email = email
        self.message = message
        self.phone = phone  # prie konstruktoriaus irgi nepamirštame pridėti:

    def __repr__(self):  # Inbuilt funkcija - šios funkcijos grąžinama reikšmė naudojama spausdinant objektą (pavyzdžiui, spausdinant šios lentelės įrašą į konsolę)
        return f'{self.name} - {self.email}'
