from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin, UserOut, Token
from app.models.auth import User
from app.auth.jwt import create_access_token
from app.db.session import get_db  

from .functions import get_password_hash, verify_password

router = APIRouter()


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
