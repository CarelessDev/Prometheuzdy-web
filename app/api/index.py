from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin, UserOut, Token
from app.models.auth import User
from app.auth.jwt import create_access_token
from app.db.session import get_db  
from passlib.context import CryptContext


router = APIRouter()

@router.get("/")
async def home():
    print("Home")
    return FileResponse("app/static/index.html")