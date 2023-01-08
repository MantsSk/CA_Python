from app import app, db, Message
from random import randint

with app.app_context():
    # NOTE: IF there are any records missing - clear the table and seed them using setupdb.py file

    all_messages = Message.query.all()
    print(all_messages)

    #  [John - john@email.com, Sean - Sean@email.com, Richy - richy@email.com, Rachel - rachel@email.com]

    message1 = Message.query.get(1)
    print(message1)

    # John - john@email.com

    message_sean = Message.query.filter_by(name='Sean')
    print(message_sean.all())

    # [Sean - Sean@email.com]

    sean = Message.query.get(2)
    sean.email = 'sean_updated@email.com'
    db.session.add(sean)
    db.session.commit()
    print(Message.query.all())

    # [John - john@email.com, Sean - sean_updated@email.com, Richy - richy@email.com, Rachel - rachel@email.com]

    john = Message.query.get(1)
    db.session.delete(john)
    db.session.commit()
    print(Message.query.all())

    # [Sean - sean_updated@email.com, Richy - richy@email.com, Rachel - rachel@email.com]

    messages = Message.query.all()

    for i in messages:
        random_phone = randint(999999, 10000000)
        i.phone = str(random_phone)
        db.session.add(i)

    db.session.commit()

    for x in messages:
        print(f'{x.id}, {x.name}, {x.email}, {x.phone}, {x.message}')

    # 2, Sean, Sean@email.com, 3169717, Content 2
    # 3, Richy, richy@email.com, 4201893, Content 3
    # 4, Rachel, rachel@email.com, 8894234, Content 4
