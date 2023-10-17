from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/register")
async def register_get():
    """
    Serves the registration page.
    
    Returns:
    - FileResponse: The HTML file for the registration page.
    """
    return FileResponse("app/static/register/index.html")


@router.get("/login")
async def login_get():
    """
    Serves the login page.
    
    Returns:
    - FileResponse: The HTML file for the login page.
    """
    return FileResponse("app/static/login/index.html")

