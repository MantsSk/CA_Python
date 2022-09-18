from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'to_do.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# DB objektas
class Uzduotis(db.Model):
    __tablename__ = 'uzduotis'
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column("Pavadinimas", db.String)
    atlikta = db.Column("Atlikta", db.Boolean)

# Užduoties schema
class UzduotisSchema(ma.Schema):
    class Meta:
        fields = ('id', 'pavadinimas', 'atlikta')

uzduotis_schema = UzduotisSchema()
uzduotys_schema = UzduotisSchema(many=True)


# Crud
@app.route('/uzduotis', methods=['POST'])
def prideti_uzduoti():
    db.create_all()
    nauja_uzduotis = Uzduotis(**request.json)
    db.session.add(nauja_uzduotis)
    db.session.commit()
    return uzduotis_schema.jsonify(nauja_uzduotis)

# cRud
@app.route('/uzduotis', methods=['GET'])
def gauti_visas_uzduotis():
    visos_uzduotys = Uzduotis.query.all()
    rezultatas = uzduotys_schema.dump(visos_uzduotys)
    return jsonify(rezultatas)

# cRud
@app.route('/uzduotis/<id>', methods=['GET'])
def gauti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    return uzduotis_schema.jsonify(uzduotis)

# crUd
@app.route('/uzduotis/<id>', methods=['PUT'])
def pakeisti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    uzduotis.pavadinimas = request.json['pavadinimas']
    uzduotis.atlikta = request.json['atlikta']
    db.session.commit()
    return uzduotis_schema.jsonify(uzduotis)

# cruD
@app.route('/uzduotis/<id>', methods=['DELETE'])
def istrinti_uzduoti(id):
    uzduotis = Uzduotis.query.get(id)
    db.session.delete(uzduotis)
    db.session.commit()
    return uzduotis_schema.jsonify(uzduotis)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    db.create_all()
