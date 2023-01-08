from app import db, Message, app

with app.app_context():  # Reikia app konteksto, nes šis failas kitaip apie jį nežino ir neveikia
    db.create_all()  # sukurs mūsų lentelę DB

    # db.session.query(Message).delete() # Jeigu reikia pravalyti lentelę

    # Iš karto inicijuosime testams keletą įrašų:
    message1 = Message('John', 'john@email.com',
                       'Content 1')
    message2 = Message('Sean', 'Sean@email.com',
                       'Content 2')
    message3 = Message('Richy', 'richy@email.com',
                       'Content 3')
    message4 = Message('Rachel', 'rachel@email.com',
                       'Content 4')

    # Pridėsime šias žinutes į mūsų DB
    db.session.add_all([message1, message2, message3, message4])

    # .commit išsaugo pakeitimus
    db.session.commit()

    print(message1.id)
    print(message2.id)
    print(message3.id)
    print(message4.id)
