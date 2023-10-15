"""
app/api/routes/user.py

This module manages the user-related routes for the FastAPI application, particularly retrieving user information. 
It utilizes FastAPI's routing, dependency injection system, and exception handling, along with SQLAlchemy for 
database interactions and JWT for authentication.

Functions:
- get_current_user: Extracts and verifies the JWT from the Authorization header and returns the payload.
- get_user: Retrieves and returns the information of the currently authenticated user.

Variables:
- security: An instance of FastAPI's HTTPBearer, used to extract the token from the request.
- router: An instance of FastAPI's APIRouter, to which the route functions are added.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt import verify_access_token
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.auth import User
from app.schemas.user import UserInfo

security = HTTPBearer()
router = APIRouter(prefix="/user")

def get_current_user(authorization: HTTPAuthorizationCredentials = Depends(security)):
    """
    Extracts and verifies the JWT from the Authorization header and returns the payload.
    
    Parameters:
    - authorization (HTTPAuthorizationCredentials): The authorization credentials from the request.
    
    Returns:
    - dict: The JWT payload if the token is valid, raises HTTPException otherwise.
    """
    token = authorization.credentials
    payload = verify_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )
    return payload

@router.get("/")
def get_user(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)) -> UserInfo:
    """
    Retrieves and returns the information of the currently authenticated user.
    
    Parameters:
    - current_user (dict): The JWT payload of the current user, obtained from the Depends dependency.
    - db (Session): The database session, obtained from the Depends dependency.
    
    Returns:
    - UserInfo: The user information retrieved from the database.
    """
    username = current_user.get("sub")
    db_user = db.query(User).filter(User.username==username).first()

    output = UserInfo(
        first_name=db_user.first_name,
        last_name=db_user.last_name,
        email=db_user.email,
        username=db_user.username
    )

    return output
