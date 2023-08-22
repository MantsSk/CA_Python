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


# Užduoties schema
class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'price', 'quantity')


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


# Crud
@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.json['title']
    price = request.json['price']
    quantity = request.json['quantity']
    new_item = Item(title=title, price=price, quantity=quantity)
    db.session.add(new_item)
    db.session.commit()
    return {'message': 'Item Created'}


# cRud
@app.route('/items', methods=['GET'])
def all_items():
    all_items = Item.query.all()
    return items_schema.jsonify(all_items)


# cRud
@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    db.create_all()
    item = Item.query.get(id)
    return item_schema.jsonify(item)


# crUd
@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get(id)
    item.title = request.json['title']
    item.price = request.json['price']
    item.quantity = request.json['quantity']
    db.session.commit()
    return {'message': 'Item updated'}


# cruD
@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return {'message': 'Item deleted'}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
