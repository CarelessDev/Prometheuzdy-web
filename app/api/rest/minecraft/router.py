from fastapi import APIRouter, Depends
from typing import List
from app.schemas.mc_server import MCServerInfo

from .endpoints.get_minecraft_server import get_minecraft_server as gms

router = APIRouter()

@router.get("/server_list")
def get_minecraft_server(server_list: List[MCServerInfo] = Depends(gms)) -> List[MCServerInfo]:
    """
    Returns a list of all Minecraft servers by querying it from database.
    
    Returns:
    - list: A list of all Minecraft servers.
    """
    return server_list



