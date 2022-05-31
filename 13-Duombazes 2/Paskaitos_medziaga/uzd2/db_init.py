from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_session = None
_engine = create_engine('sqlite:///darbuotojas2.db')
Base = declarative_base()


def init_session():
    global _engine
    Session = sessionmaker(bind=_engine)
    Base.metadata.create_all(_engine)
    global _session
    _session = Session()
    return _session


def close_session():
    global _session
    global _engine
    _session.close()

