import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime
import forms

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'biudzetas.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Irasas(db.Model):
    __tablename__ = "irasas"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column("Data", DateTime, default=datetime.now())
    pajamos = db.Column("Pajamos", db.Boolean)
    suma = db.Column("Vardas", db.Integer)


@app.route("/")
def records():
    try:
        visi_irasai = Irasas.query.all()
    except:
        visi_irasai = []
    return render_template("index.html", visi_irasai=visi_irasai, datetime=datetime)

@app.route("/naujas_irasas", methods=["GET", "POST"])
def new_record():
    db.create_all()
    forma = forms.IrasasForm()
    if forma.validate_on_submit():
        naujas_irasas = Irasas(pajamos=forma.pajamos.data, suma=forma.suma.data)
        db.session.add(naujas_irasas)
        db.session.commit()
        return redirect(url_for('records'))
    return render_template("prideti_irasa.html", form=forma)


@app.route("/delete/<int:id>")
def delete(id):
    irasas = Irasas.query.get(id)
    db.session.delete(irasas)
    db.session.commit()
    return redirect(url_for('records'))

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    forma = forms.IrasasForm()
    irasas = Irasas.query.get(id)
    if forma.validate_on_submit():
        irasas.pajamos = forma.pajamos.data
        irasas.suma = forma.suma.data
        db.session.commit()
        return redirect(url_for('records'))
    return render_template("update.html", form=forma, irasas=irasas)

@app.route("/balansas")
def balance():
    try:
        visi_irasai = Irasas.query.all()
    except:
        visi_irasai = []
    balansas = 0
    for irasas in visi_irasai:
        if irasas.pajamos:
            balansas += irasas.suma
        else:
            balansas -= irasas.suma
    return render_template("balansas.html", balansas=balansas)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()
