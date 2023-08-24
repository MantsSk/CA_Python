from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from irasai import db, app

class Irasas(db.Model):
    __tablename__ = "irasas"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column("Data", db.DateTime)
    irasas = db.Column("irasas", db.String(20))
    vartotojas_id = db.Column(db.Integer, db.ForeignKey("vartotojas.id"))
    vartotojas = db.relationship("Vartotojas", backref="irasai")

class Vartotojas(db.Model, UserMixin):
    __tablename__ = "vartotojas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String(20), unique=True, nullable=False)
    el_pastas = db.Column("El.Pastas", db.String(120), unique=True, nullable=False)
    nuotrauka = db.Column("Nuotrauka", db.String(20), nullable=False, default="default.jpg")
    slaptazodis = db.Column("Slaptazodis", db.String(60), unique=True, nullable=False)

    def get_reset_token(self, expires_sec=600):
        s = Serializer(app.config["SECRET_KEY"], expires_sec)
        print("id yra", self.id)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Vartotojas.query.get(user_id)
