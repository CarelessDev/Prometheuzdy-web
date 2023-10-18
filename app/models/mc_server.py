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

    __tablename__ = "mc_servers"

    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String)
    server_ip = Column(String)
    server_port = Column(Integer)
    server_version = Column(String)
    server_note = Column(String)
    ssh_username = Column(String)
    ssh_port = Column(Integer)
    ssh_public_key = Column(String)
    start_cmd = Column(String)
    stop_cmd = Column(String)
