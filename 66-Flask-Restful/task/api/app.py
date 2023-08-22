from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'sqlite.db')

db = SQLAlchemy(app)
ma = Marshmallow(app)
Migrate(app, db)


# DB objektas
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    price = db.Column('price', db.Float)
    quantity = db.Column('quantity', db.Integer)


# Sukurkite schemą
class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'price', 'quantity')


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


# Sukurti įrašo sukūrimo endpointą
@app.route('/items/new', methods=['POST'])
def add_item():
    # Kodą rašyti čia
    return {'message': 'Item created!'}


# Sukurti visų įrašų informacijos grąžinimo endpointą
@app.route('/items', methods=['GET'])
def all_items():
    # Kodą rašyti čia

    # Vietoje None reikia grąžinti visus įrašus
    return None


# Sukurti vieno įrašo informacijos grąžinimo endpointą
@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    # Kodą rašyti čia

    # Vietoje None reikia grąžinti įrašą
    return None


# Sukurti atnaujinimo endpoint'ą
@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    # Kodą rašyti čia
    return {'message': 'Item updatedĄ'}


# Sukurti ištrynimo endpoint'ą
@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    # Kodą rašyti čia
    return {'message': 'Item deleted!'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
