from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from db import db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column("username", String(20), unique=True, nullable=False)
    email = Column("email", String(120), unique=True, nullable=False)
    password = Column("password", String(60), unique=True, nullable=False)
    avatar = Column(String(20), nullable=False, default='default.jpg')
