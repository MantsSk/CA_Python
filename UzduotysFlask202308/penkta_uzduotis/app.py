from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import forms

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///darbas.db'
db = SQLAlchemy(app)
Migrate(app, db)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

association_table = db.Table('darbuotojas_departamentas', db.metadata,
                             db.Column('id', db.Integer, primary_key=True),
                             db.Column('darbuotojo_id', db.Integer,
                                       db.ForeignKey('darbuotojas.id')),
                             db.Column('departamento_id', db.Integer,
                                       db.ForeignKey('departamentas.id'))
                             )


class Darbuotojas(db.Model):
    __tablename__ = 'darbuotojas'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column('vardas', db.String)
    pavarde = db.Column('pavarde', db.String)
    departamentai = db.relationship(
        'Departamentas', secondary=association_table, back_populates='darbuotojai')


class Departamentas(db.Model):
    __tablename__ = 'departamentas'
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column('pavadinimas', db.String)
    darbuotojai = db.relationship(
        'Darbuotojas', secondary=association_table, back_populates='departamentai')


@app.route('/darbuotojai')
def darbuotojai():
    darbuotojai = Darbuotojas.query.all()
    return render_template('darbuotojai.html', visi_darbuotojai=darbuotojai)


@app.route('/departamentai')
def departamentai():
    departamentai = Departamentas.query.all()
    return render_template('departamentai.html', visi_departamentai=departamentai)


@app.route('/departamentai/istrinti/<int:id>')
def istrinti_departamenta(id):
    return redirect(url_for('departamentai'))


@app.route('/darbuotojai/istrinti/<int:id>')
def istrinti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get(id)
    db.session.delete(darbuotojas)
    db.session.commit()
    return redirect(url_for('darbuotojai'))


@app.route('/darbuotojai/naujas', methods=['GET', 'POST'])
def sukurti_darbuotoja():
    forma = forms.DarbuotojasForm()
    if forma.validate_on_submit():
        naujas_darbuotojas = Darbuotojas(vardas=forma.vardas.data,
                                         pavarde=forma.pavarde.data)
        for departamentas in forma.departamentai.data:
            priskirtas_departamentas = Departamentas.query.get(
                departamentas.id)
            naujas_darbuotojas.departamentai.append(priskirtas_departamentas)
        db.session.add(naujas_darbuotojas)
        db.session.commit()
        return redirect(url_for('darbuotojai'))
    return render_template('sukurti_darbuotoja.html', forma=forma)


@app.route('/departamentai/naujas', methods=['GET', 'POST'])
def sukurti_departamenta():
    forma = forms.DepartamentasForm()
    if forma.validate_on_submit():
        naujas_departamentas = Departamentas(
            pavadinimas=forma.pavadinimas.data)
        for darbuotojas in forma.darbuotojai.data:
            priskirtas_darbuotojas = Darbuotojas.query.get(
                darbuotojas.id)
            naujas_departamentas.darbuotojai.append(priskirtas_darbuotojas)
        db.session.add(naujas_departamentas)
        db.session.commit()
        return redirect(url_for('departamentai'))
    return render_template('sukurti_departamenta.html', forma=forma)


@app.route("/darbuotojai/atnaujinti/<int:id>", methods=['GET', 'POST'])
def atnaujinti_darbuotoja(id):
    forma = forms.DarbuotojasForm()
    darbuotojas = Darbuotojas.query.get(id)
    if forma.validate_on_submit():
        darbuotojas.vardas = forma.vardas.data
        darbuotojas.pavarde = forma.pavarde.data
        darbuotojas.departamentai = []
        for departamentas in forma.departamentai.data:
            priskirtas_departamentas = Departamentas.query.get(
                departamentas.id)
            darbuotojas.departamentai.append(priskirtas_departamentas)
        db.session.commit()
        return redirect(url_for('darbuotojai'))
    return render_template("atnaujinti_darbuotoja.html", forma=forma, darbuotojas=darbuotojas)


@app.route("/departamentai/atnaujinti/<int:id>", methods=['GET', 'POST'])
def atnaujinti_departamenta(id):
    forma = forms.DepartamentasForm()
    departamentas = Departamentas.query.get(id)
    if forma.validate_on_submit():
        departamentas.pavadinimas = forma.pavadinimas.data
        departamentas.darbuotojai = []
        for darbuotojas in forma.darbuotojai.data:
            priskirtas_darbuotojas = Darbuotojas.query.get(
                darbuotojas.id)
            departamentas.darbuotojai.append(priskirtas_darbuotojas)
        db.session.commit()
        return redirect(url_for('departamentai'))
    return render_template("atnaujinti_departamenta.html", forma=forma, departamentas=departamentas)


if __name__ == '__main__':
    app.run(debug=True)
