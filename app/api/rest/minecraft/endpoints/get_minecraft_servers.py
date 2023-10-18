from fastapi import Depends
from app.db.session import get_db
from sqlalchemy.orm import Session
from typing import List
from app.models.mc_server import MCServer
from app.schemas.mc_server import MCServerInfo

def get_minecraft_servers(db: Session = Depends(get_db)) -> List[MCServerInfo]:
    """
    Returns a list of all Minecraft servers by querying it from database.
    
    Returns:
    - list: A list of all Minecraft servers.
    """
    return db.query(MCServer).all()
