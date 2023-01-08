from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
# from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField

import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite?check_same_thread=False')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "codeacademytest18@gmail.com"
app.config['MAIL_PASSWORD'] = "knokaugbfzuitxfj"
db = SQLAlchemy(app)
db.init_app(app)


association_table = db.Table('association', db.metadata,
                             db.Column('tevas_id', db.Integer,
                                       db.ForeignKey('tevas.id')),
                             db.Column('vaikas_id', db.Integer,
                                       db.ForeignKey('vaikas.id'))
                             )


class Tevas(db.Model):
    __tablename__ = 'tevas'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    vaikai = db.relationship("Vaikas", secondary=association_table,
                             back_populates="tevai")


class Vaikas(db.Model):
    __tablename__ = 'vaikas'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    tevai = db.relationship("Tevas", secondary=association_table,
                            back_populates="vaikai")


def query_tevai():
    with app.app_context():
        return Tevas.query.all()


def query_vaikai():
    with app.app_context():
        return Vaikas.query.all()


class TevasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    vaikai = QuerySelectMultipleField(
        query_factory=query_vaikai, get_label="vardas")
    submit = SubmitField('Įvesti')


class VaikasForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavardė', [DataRequired()])
    tevai = QuerySelectMultipleField(
        query_factory=query_tevai, get_label="vardas")
    submit = SubmitField('Įvesti')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tevai")
def parents():
    try:
        visi_tevai = Tevas.query.all()
    except:
        visi_tevai = []
    return render_template("tevai.html", visi_tevai=visi_tevai)


@app.route("/vaikai")
def children():
    try:
        visi_vaikai = Vaikas.query.all()
    except:
        visi_vaikai = []
    return render_template("vaikai.html", visi_vaikai=visi_vaikai)


@app.route("/naujas_tevas", methods=["GET", "POST"])
def new_parent():
    db.create_all()
    forma = TevasForm()
    if forma.validate_on_submit():
        naujas_tevas = Tevas(vardas=forma.vardas.data,
                             pavarde=forma.pavarde.data)
        for vaikas in forma.vaikai.data:
            priskirtas_vaikas = Vaikas.query.get(vaikas.id)
            naujas_tevas.vaikai.append(priskirtas_vaikas)
        db.session.add(naujas_tevas)
        db.session.commit()
        return redirect(url_for('parents'))
    return render_template("prideti_teva.html", form=forma)


@app.route("/naujas_vaikas", methods=["GET", "POST"])
def new_child():
    db.create_all()
    forma = VaikasForm()
    if forma.validate_on_submit():
        naujas_vaikas = Vaikas(vardas=forma.vardas.data,
                               pavarde=forma.pavarde.data)
        for tevas in forma.tevai.data:
            priskirtas_tevas = Tevas.query.get(tevas.id)
            naujas_vaikas.tevai.append(priskirtas_tevas)
        db.session.add(naujas_vaikas)
        db.session.commit()
        return redirect(url_for('children'))
    return render_template("prideti_vaika.html", form=forma)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    with app.app_context():
        db.create_all()
