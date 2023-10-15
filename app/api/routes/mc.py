"""
app/api/routes/mc.py

This module manages the Minecraft server-related route for the FastAPI application, particularly serving a static HTML 
page related to Minecraft server details. It utilizes FastAPI's routing and response classes to manage HTTP requests 
and responses.

Functions:
- get_mc: Serves a static HTML page related to Minecraft server details.
"""

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(prefix="/mc")

@router.get("/")
def get_mc():
    """
    Serves a static HTML page related to Minecraft server details.
    
    Returns:
    - FileResponse: An instance of FastAPI's FileResponse, serving the specified HTML file.
    """
    return FileResponse("app/static/mc/index.html")
