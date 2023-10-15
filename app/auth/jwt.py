"""
auth/jwt.py

This module is responsible for handling JSON Web Tokens (JWT) for user authentication within the FastAPI application. 
It utilizes the python-jose library to encode and decode JWT, and python-dotenv to manage environment variables.

Functions:
- create_access_token: Generates a JWT using user data and expiration details.
- verify_access_token: Validates the JWT and returns the payload if valid.

Variables:
- SECRET_KEY: The secret key used to encode and decode JWT.
- ALGORITHM: The algorithm used for the JWT encoding and decoding.
- ACCESS_TOKEN_EXPIRE_MINUTES: The duration in minutes for which the access token is valid.

Dependencies:
- jose: A library used for encoding, decoding, and verifying JWT.
- datetime: A module to work with dates and times.
- timedelta: A class for representing differences between dates.
- Optional: A special typing construct to denote optional values.
- load_dotenv: A function to load environment variables from a file.
- HTTPException: An exception class for HTTP status codes.
- os: A module providing a way of using operating system dependent functionality.
"""

from jose import JWSError, jwt
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv
from fastapi import HTTPException
import os

# Load environment variables from the specified file.
load_dotenv("environments/auth.env")

# Retrieve environment variables related to JWT.
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data: dict) -> str:
    """
    Generates a JWT using the provided user data and expiration details.
    
    Parameters:
    - data (dict): The data to encode into the JWT.
    
    Returns:
    - str: The encoded JWT.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str) -> Optional[dict]:
    """
    Validates the provided JWT and returns the payload if valid. Raises an HTTPException if the token is invalid.
    
    Parameters:
    - token (str): The JWT to validate.
    
    Returns:
    - Optional[dict]: The decoded JWT payload if valid, None otherwise.
    """
    credentials_exception = HTTPException(
        status_code=401, 
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWSError:
        raise credentials_exception
