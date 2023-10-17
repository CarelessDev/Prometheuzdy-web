"""
models/mc_server.py

This module defines the data model for Minecraft server entities within the application, utilizing SQLAlchemy as the 
ORM (Object-Relational Mapper). The MCServer model contains fields relevant for storing details about a Minecraft 
server.

Classes:
- MCServer: Represents a Minecraft server entity with attributes detailing the server's properties.
"""

from sqlalchemy import Column, Integer, String
from app.db.session import Base

class MCServer(Base):
    """
    Represents a Minecraft server entity within the application. 
    
    Attributes:
    - __tablename__ (str): The name of the table in the database.
    - id (Column): The unique identifier for a server, primary key.
    - server_name (Column): The name of the Minecraft server.
    - server_ip (Column): The IP address of the Minecraft server.
    - server_port (Column): The port number of the Minecraft server.
    - server_version (Column): The version of the Minecraft server.
    - server_executable (Column): The path or name of the server's executable file.
    """
    
    __tablename__ = "mc_servers"

    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String)
    server_ip = Column(String)
    server_port = Column(Integer)
    server_version = Column(String)
    server_executable = Column(String)
    server_note = Column(String)
    ssh_username = Column(String)
    ssh_port = Column(Integer)
