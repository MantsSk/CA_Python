import os
from flask import Flask, render_template, request, redirect, url_for
from forms import StudentuForma
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


class Studentai(db.Model):
    __tablename__ = 'studentai'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(80), nullable=False)
    pavarde = db.Column(db.String(120), nullable=False)
    el_pastas = db.Column(db.String(40), nullable=False)

    def __init__(self, vardas, pavarde, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.el_pastas = el_pastas

    def __repr__(self):
        return f'{self.vardas} - {self.pavarde}'


@app.route('/studentai')
def studentai():
    studentai = Studentai.query.all()
    print(studentai)
    return render_template('studentai.html', studentai=studentai)


@app.route('/studentai/<string:id>')
def studentas(id):
    studentas = Studentai.query.get(id)
    return render_template('studentas.html', studentas=studentas)


@app.route('/studentai/naujas', methods=['GET', 'POST'])
def naujas_studentas():
    forma = StudentuForma()
    if forma.validate_on_submit():
        naujas_studentas = Studentai(
            vardas=forma.vardas.data, pavarde=forma.pavarde.data, el_pastas=forma.el_pastas.data)
        db.session.add(naujas_studentas)
        db.session.commit()
        return redirect(url_for('studentai'))
    return render_template('naujas_studentas.html', forma=forma)


@app.route('/studentai/istrinti/<int:id>')
def istrinti_studenta(id):
    studentas = Studentai.query.get(id)
    db.session.delete(studentas)
    db.session.commit()
    return redirect(url_for('naujas_studentas'))


@app.route("/studentai/atnaujinti/<int:id>", methods=['GET', 'POST'])
def atnaujinti_studenta(id):
    forma = StudentuForma()
    studentas = Studentai.query.get(id)
    if forma.validate_on_submit():
        studentas.vardas = forma.vardas.data
        studentas.pavarde = forma.pavarde.data
        studentas.el_pastas = forma.el_pastas.data
        db.session.commit()
        return redirect(url_for('studentai'))
    return render_template('atnaujinti_studenta.html', forma=forma, studentas=studentas)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)
