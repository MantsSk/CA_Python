
import os
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)

db = SQLAlchemy()

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'vaikaitevai.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


class Tevas(db.Model):
    __tablename__ = "tevas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    vaikas_id = db.Column(db.Integer, db.ForeignKey("vaikas.id"))
    vaikas = db.relationship("Vaikas", back_populates="tevai")


class Vaikas(db.Model):
    __tablename__ = "vaikas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    tevai = db.relationship("Tevas", back_populates="vaikas")


@app.route("/")
def index():
    with app.app_context():
        db.create_all()

    child = Vaikas(vardas="Mantas", pavarde="Skara")

    parent = Tevas(vardas="Arunas", pavarde="Skara")
    parent.vaikas = child

    print(parent.vaikas)
    print(child.tevai)

    db.session.add(parent)
    db.session.commit()

    return render_template("index.html")

    # child.tevai = parent
    # print(parent.vaikas)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
