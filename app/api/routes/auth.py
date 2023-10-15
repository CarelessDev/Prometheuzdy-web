"""
app/api/routes/auth.py

This module manages the authentication routes for the FastAPI application, handling user registration and login 
functionality. It utilizes FastAPI's routing, dependency injection system, and exception handling, along with 
SQLAlchemy for database interactions.

Functions:
- verify_password: Verifies if a plain password matches its hashed version.
- get_password_hash: Returns the hashed version of a provided password.
- register_get: Serves the registration page.
- register_post: Handles user registration, adding new users to the database.
- login_get: Serves the login page.
- login_post: Handles user login, verifying credentials, and issuing JWTs.

Variables:
- router: An instance of FastAPI's APIRouter, to which the route functions are added.
- pwd_context: An instance of passlib's CryptContext, configured to use bcrypt hashing.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin, UserOut, Token
from app.models.auth import User
from app.auth.jwt import create_access_token
from app.db.session import get_db  
from passlib.context import CryptContext


router = APIRouter(prefix="/auth")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """
    Verifies if a plain password matches its hashed version.
    
    Parameters:
    - plain_password (str): The password in plain text.
    - hashed_password (str): The hashed version of the password.
    
    Returns:
    - bool: True if passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    Returns the hashed version of a provided password.
    
    Parameters:
    - password (str): The password in plain text.
    
    Returns:
    - str: The hashed version of the password.
    """
    return pwd_context.hash(password)

@router.get("/register")
async def register_get():
    """
    Serves the registration page.
    
    Returns:
    - FileResponse: The HTML file for the registration page.
    """
    return FileResponse("app/static/register/index.html")

@router.post("/register", response_model=UserOut)
async def register_post(user: UserCreate, db: Session = Depends(get_db)):
    """
    Handles user registration, adding new users to the database.
    
    Parameters:
    - user (UserCreate): The user details to register.
    - db (Session): The database session.
    
    Returns:
    - UserOut: The created user's details.
    """
    db_user = db.query(User).filter(User.username == user.username).first()
    
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered."
        )
    
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        hashed_password=hashed_password,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    return new_user

@router.get("/login")
async def login_get():
    """
    Serves the login page.
    
    Returns:
    - FileResponse: The HTML file for the login page.
    """
    return FileResponse("app/static/login/index.html")

@router.post("/login", response_model=Token)
async def login_post(user: UserLogin, db: Session = Depends(get_db)):
    """
    Handles user login, verifying credentials, and issuing JWTs.
    
    Parameters:
    - user (UserLogin): The user details to verify.
    - db (Session): The database session.
    
    Returns:
    - Token: The issued JWT upon successful authentication.
    """

    db_user = db.query(User).filter(User.username==user.username).first()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password."
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
