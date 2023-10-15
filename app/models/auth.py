"""
auth/models.py

This module defines the data model for User entities within the application, utilizing SQLAlchemy as the ORM 
(Object-Relational Mapper). The User model contains fields relevant for user authentication and identification.

Classes:
- User: Represents a user entity with attributes necessary for authentication and identification within the application.
"""

from sqlalchemy import Column, Integer, String
from app.db.session import Base

class User(Base):
    """
    Represents a user entity within the application. 
    
    Attributes:
    - __tablename__ (str): The name of the table in the database.
    - id (Column): The unique identifier for a user, primary key.
    - username (Column): The username of the user, must be unique.
    - hashed_password (Column): The hashed version of the user's password.
    """
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

