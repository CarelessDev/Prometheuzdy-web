from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.auth import User
from app.schemas.user import UserInfo
from .functions import get_current_user

router = APIRouter()

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
