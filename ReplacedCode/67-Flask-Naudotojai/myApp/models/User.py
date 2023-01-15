from flask_login import UserMixin
from flask_sqlalchemy import Model
from sqlalchemy import Column, Integer, String

from db import db


class User(db.Model, UserMixin):
    __tablename__ = "vartotojas"
    id = Column(Integer, primary_key=True)
    username = Column("username", String(20), unique=True, nullable=False)
    email = Column("email", String(120), unique=True, nullable=False)
    password = Column("password", String(60), unique=True, nullable=False)
