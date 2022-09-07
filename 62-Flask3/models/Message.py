from db import db


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(40), unique=True)  # Papildome duomenų bazės modelį nauju stulpeliu.
    message = db.Column(db.Text, nullable=False)

    # prie konstruktoriaus irgi nepamirštame pridėti:
    def __init__(self, name, email, message, phone):
        self.name = name
        self.email = email
        self.message = message
        self.phone = phone

    def __repr__(self):
        return f'{self.name} - {self.email}'

