from message_example import Message, db

# CREATE
Styvas = Message('Styvas', 'styvas@yahoo.com', 'I am Steve.')
db.session.add(Styvas)
db.session.commit() 

# READ
print(Message.query.all()) # [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com, Styvas - styvas@yahoo.com]
print(Message.query.get(2)) # Antanas - antanas@mail.lt

# UPDATE
Message.query.get(2).name = "Rodas"
db.session.commit() 
print(Message.query.get(2)) # Read operatiion for seeing changes, Rodas - antanas@mail.lt

# DELETE
db.session.delete(Message.query.get(2))
db.session.commit()
print(Message.query.get(2)) # 'NoneType' object has no attribute 'name'