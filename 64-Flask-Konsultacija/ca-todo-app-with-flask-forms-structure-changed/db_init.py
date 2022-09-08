from app import db, app

with app.app_context():
    db.create_all()


# Iš karto inicijuosime testams keletą įrašų:
# jonas = Query('Jonas', 'jonas@mail.com', 'Kažkoks labai rimtas atsiliepimas.')
# antanas = Query('Antanas', 'antanas@mail.lt', 'Antano nuomonė labai svarbi.')
# juozas = Query('Juozas', 'juozukas@friends.lt', 'Aš labai piktas, nes blogai.')
# bronius = Query('Bronius', 'bronka@yahoo.com', 'Aš tai linksmas esu, man patinka.')

# # Pridėsime šiuos veikėjus į mūsų DB
# db.session.add_all([jonas, antanas, juozas, bronius])
# # .commit išsaugo pakeitimus
# db.session.commit()

# print(jonas.id)
# print(antanas.id)
# print(bronius.id)
# print(juozas.id)