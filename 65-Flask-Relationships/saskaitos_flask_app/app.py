import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'biudzetas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Zmogus(db.Model):
    __tablename__ = "zmogus"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    asmens_kodas = db.Column("Asmens kodas", db.String)
    tel_numeris = db.Column("Telefono numeris", db.String)

class Bankas(db.Model):
    __tablename__ = "bankas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    adresas = db.Column("Adresas", db.String)
    banko_kodas = db.Column("Banko kodas", db.String)
    swift = db.Column("SWIFT kodas", db.String)

class Saskaita(db.Model):
    __tablename__ = "saskaita"
    id = db.Column(db.Integer, primary_key=True)
    numeris = db.Column("Pavadinimas", db.String)
    zmogus_id = db.Column(db.Integer, db.ForeignKey("zmogus.id"))
    zmogus = db.relationship("Zmogus")
    bankas_id = db.Column(db.Integer, db.ForeignKey("bankas.id"))
    bankas = db.relationship("Bankas")
    balansas = db.Column("Balansas", db.Float)

@app.route("/")
def accounts():
    try:
        visos_saskaitos = Saskaita.query.all()
    except:
        visos_saskaitos = []
    return render_template("saskaitos.html", visos_saskaitos=visos_saskaitos)

@app.route("/bankai")
def banks():
    try:
        visi_bankai = Bankas.query.all()
    except:
        visi_bankai = []
    return render_template("bankai.html", visi_bankai=visi_bankai)

@app.route("/zmones")
def people():
    try:
        visi_zmones = Zmogus.query.all()
    except:
        visi_zmones = []
    return render_template("zmones.html", visi_zmones=visi_zmones)


@app.route("/naujas_zmogus", methods=["GET", "POST"])
def zmogus_new():
    db.create_all()
    forma = forms.ZmogusForm()
    if forma.validate_on_submit():
        naujas_zmogus = Zmogus(vardas=forma.vardas.data, pavarde=forma.pavarde.data, asmens_kodas=forma.asmens_kodas.data, tel_numeris=forma.tel_numeris.data)
        db.session.add(naujas_zmogus)
        db.session.commit()
        return redirect(url_for('people'))
    return render_template("prideti_zmogu.html", form=forma)

@app.route("/naujas_bankas", methods=["GET", "POST"])
def bankas_new():
    db.create_all()
    forma = forms.BankasForm()
    if forma.validate_on_submit():
        naujas_bankas = Bankas(pavadinimas=forma.pavadinimas.data, adresas=forma.adresas.data, banko_kodas=forma.banko_kodas.data, swift=forma.swift.data)
        db.session.add(naujas_bankas)
        db.session.commit()
        return redirect(url_for('banks'))
    return render_template("prideti_banka.html", form=forma)

@app.route("/nauja_saskaita", methods=["GET", "POST"])
def saskaita_new():
    db.create_all()
    forma = forms.SaskaitaForm()
    if forma.validate_on_submit():
        nauja_saskaita = Saskaita(numeris=forma.numeris.data, zmogus_id=forma.zmogus.data.id, bankas_id=forma.bankas.data.id, balansas=forma.balansas.data)
        db.session.add(nauja_saskaita)
        db.session.commit()
        return redirect(url_for('accounts'))
    return render_template("prideti_saskaita.html", form=forma)

@app.route("/zmogus_delete/<int:id>")
def zmogus_delete(id):
    uzklausa = Zmogus.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('people'))

@app.route("/bankas_delete/<int:id>")
def bankas_delete(id):
    uzklausa = Bankas.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('banks'))

@app.route("/saskaita_delete/<int:id>")
def saskaita_delete(id):
    uzklausa = Saskaita.query.get(id)
    db.session.delete(uzklausa)
    db.session.commit()
    return redirect(url_for('accounts'))

@app.route("/zmogus_update/<int:id>", methods=['GET', 'POST'])
def zmogus_update(id):
    form = forms.ZmogusForm()
    zmogus = Zmogus.query.get(id)
    if form.validate_on_submit():
        zmogus.vardas = form.vardas.data
        zmogus.pavarde = form.pavarde.data
        zmogus.asmens_kodas = form.asmens_kodas.data
        zmogus.tel_numeris = form.tel_numeris.data
        db.session.commit()
        return redirect(url_for('people'))
    return render_template("zmogus_update.html", form=form, zmogus=zmogus)


@app.route("/bankas_update/<int:id>", methods=['GET', 'POST'])
def bankas_update(id):
    form = forms.BankasForm()
    bankas = Bankas.query.get(id)
    if form.validate_on_submit():
        bankas.pavadinimas = form.pavadinimas.data
        bankas.adresas = form.adresas.data
        bankas.banko_kodas = form.banko_kodas.data
        bankas.swift = form.swift.data
        db.session.commit()
        return redirect(url_for('people'))
    return render_template("bankas_update.html", form=form, bankas=bankas)

@app.route("/saskaita_update/<int:id>", methods=['GET', 'POST'])
def saskaita_update(id):
    form = forms.SaskaitaForm()
    saskaita = Saskaita.query.get(id)
    if form.validate_on_submit():
        saskaita.numeris = form.numeris.data
        saskaita.zmogus_id = form.zmogus.data.id
        saskaita.bankas_id = form.bankas.data.id
        saskaita.balansas = form.balansas.data
        db.session.commit()
        return redirect(url_for('accounts'))
    return render_template("saskaita_update.html", form=form, saskaita=saskaita)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()