from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.jwt import verify_access_token

security = HTTPBearer()

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