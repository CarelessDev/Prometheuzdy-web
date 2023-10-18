from fastapi import APIRouter, Depends, Header
from typing import List
from app.schemas.mc_server import MCServerInfo, MCServerInitiateResponse, MCServerTerminateResponse
from .endpoints.get_minecraft_servers import get_minecraft_servers as gmss
from .endpoints.start_minecraft_server import start_minecraft_server as sms
from .endpoints.stop_minecraft_server import stop_minecraft_server as stms

router = APIRouter()

@router.get("/server/list")
def get_minecraft_server(server_list: List[MCServerInfo] = Depends(gmss)):
    """
    Returns a list of all Minecraft servers by querying it from database.
    
    Returns:
    - list: A list of all Minecraft servers.
    """
    return server_list


@router.post("/server/start")
def start_minecraft_server(response: MCServerInitiateResponse = Depends(sms)):
    """
    Starts a Minecraft server by server_id.
    """
    return response


@router.post("/server/stop")
def stop_minecraft_server(response: MCServerTerminateResponse = Depends(stms)):
    """
    Stops a Minecraft server by server_id.
    """
    return response
