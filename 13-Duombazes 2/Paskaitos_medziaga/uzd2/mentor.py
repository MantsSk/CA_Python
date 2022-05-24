from sqlalchemy import Column, Integer, String, create_engine
from db_init import Base


class Mentor(Base):
    __tablename__ = 'Mentor'
    id = Column(Integer, primary_key=True)
    mentor_id = Column("Mentor_id", Integer)
    student_id = Column("Student_id", Integer)

    def __init__(self, mentor_id, student_id):
        self.mentor_id = mentor_id
        self.student_id = student_id
