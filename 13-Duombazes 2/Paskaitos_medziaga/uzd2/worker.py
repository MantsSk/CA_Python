from sqlalchemy import Column, Integer, String, create_engine
from db_init import Base


class Worker(Base):
    __tablename__ = 'Worker'
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    last_name = Column("Surname", String)
    position = Column("Position", String)

    def __init__(self, name, last_name, position):
        self.name = name
        self.last_name = last_name
        self.position = position
