import os
from flask import Flask, render_template, request, redirect, url_for
from forms import DarbuotojuForma
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ikjasoidjapsodjjnzjkxcvbniuwhdouwheuqwheuahpuhaisdhaisughs'

db = SQLAlchemy(app)

Migrate(app, db)


class Darbuotojai(db.Model):
    __tablename__ = 'darbuotojai'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(80), nullable=False)
    pavarde = db.Column(db.String(120), nullable=False)
    el_pastas = db.Column(db.String(40), nullable=False)
    tel_numeris = db.Column(db.String(40), nullable=False)
    alga = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, vardas, pavarde, el_pastas, tel_numeris, alga):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas
        self.tel_numeris = tel_numeris
        self.alga = alga

    def __repr__(self):
        return f'{self.vardas} - {self.pavarde}'


@app.route('/')
@app.route('/darbuotojai')
def darbuotojai():
    darbuotojai = Darbuotojai.query.all()
    return render_template('darbuotojai.html', darbuotojai=darbuotojai)


@app.route('/darbuotojai/<string:id>')
def darbuotojas(id):
    darbuotojas = Darbuotojai.query.get(id)
    return render_template('darbuotojas.html', darbuotojas=darbuotojas)


@app.route('/darbuotojai/naujas', methods=['GET', 'POST'])
def naujas_darbuotojas():
    forma = DarbuotojuForma()
    if forma.validate_on_submit():
        naujas_darbuotojas = Darbuotojai(
            vardas=forma.vardas.data, pavarde=forma.pavarde.data, el_pastas=forma.el_pastas.data, tel_numeris=forma.tel_numeris.data, alga=forma.alga.data)
        db.session.add(naujas_darbuotojas)
        db.session.commit()
        return redirect(url_for('darbuotojai'))
    return render_template('naujas_darbuotojas.html', forma=forma)


@app.route('/darbuotojai/istrinti/<int:id>')
def istrinti_darbuotoja(id):
    darbuotojas = Darbuotojai.query.get(id)
    db.session.delete(darbuotojas)
    db.session.commit()
    return redirect(url_for('darbuotojai'))


@app.route("/darbuotojai/atnaujinti/<int:id>", methods=['GET', 'POST'])
def atnaujinti_darbuotoja(id):
    forma = DarbuotojuForma()
    darbuotojas = Darbuotojai.query.get(id)
    if forma.validate_on_submit():
        darbuotojas.vardas = forma.vardas.data
        darbuotojas.pavarde = forma.pavarde.data
        darbuotojas.el_pastas = forma.el_pastas.data
        darbuotojas.tel_numeris = forma.tel_numeris.data
        darbuotojas.alga = forma.alga.data
        db.session.commit()
        return redirect(url_for('darbuotojas', id=darbuotojas.id))
    return render_template('atnaujinti_darbuotoja.html', forma=forma, darbuotojas=darbuotojas)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
