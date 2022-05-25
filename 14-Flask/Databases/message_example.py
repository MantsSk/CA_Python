from email import message
from email.mime import base
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# pilnas kelias iki šio failo.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# nustatėme, kad mūsų duomenų bazė bus šalia šio failo esants data.sqlite failas
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# neseksime kiekvienos modifikacijos
db = SQLAlchemy(app)

class Message(db.Model):
    # DB lentelei priskiria pavadinimą, jei nenurodysite, priskirs automatiškai pagal klasės pavadinimą.
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)  # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

    def __repr__(self):
        return f'{self.name} - {self.email}'

db.create_all()  # sukurs mūsų lentelę DB

# Iš karto inicijuosime testams keletą įrašų:
jonas = Message('Jonas', 'jonas@mail.com', 'Kažkoks labai rimtas atsiliepimas.')
antanas = Message('Antanas', 'antanas@mail.lt', 'Antano nuomonė labai svarbi.')
juozas = Message('Juozas', 'juozukas@friends.lt', 'Aš labai piktas, nes blogai.')
bronius = Message('Bronius', 'bronka@yahoo.com', 'Aš tai linksmas esu, man patinka.')

# Pridėsime šiuos veikėjus į mūsų DB

db.session.add_all([jonas, antanas, juozas, bronius])
# .commit išsaugo pakeitimus
db.session.commit()

message_query = Message.query.all()
print(message_query[2])

if __name__ == "__main__":
    app.run(debug=True)

