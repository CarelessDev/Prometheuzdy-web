"""
db/session.py

This module sets up the SQLAlchemy engine and session to interact with the database.

- `create_engine`: Establishes a connection to the database.
- `sessionmaker`: Creates a factory to produce database sessions.
- `DBConfig`: Retrieves database configuration (like the URI).
- `engine`: An instance to interact with the database.
- `SessionLocal`: A factory to create new database sessions for interactions.

In practice, `SessionLocal()` is used to create a session, interact with the database, and is closed after use.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.db_config import DBConfig



db_config = DBConfig()
engine = create_engine(db_config.sqlalchemy_database_uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
