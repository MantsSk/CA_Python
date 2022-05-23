from projektas import engine, Projektas
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

#sunukiai = Projektas(name="Kebabine", price=10_000)
#session.add(sunukiai)
#session.commit()

sunukiai = session.query(Projektas).filter(Projektas.price > 5_000).filter(Projektas.name=="Dog hairdresser").all()
sunukiai[0].price = 15_000
session.commit()
pass
