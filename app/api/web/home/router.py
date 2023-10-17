from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/")
async def home():
    print("Home")
    return FileResponse("app/static/index.html")