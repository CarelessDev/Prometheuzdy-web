"""
auth/schemas.py

This module defines Pydantic models for user creation and login within the application. These models are utilized to 
validate and structure the data payload in HTTP requests related to user management.

Classes:
- UserCreate: A Pydantic model defining the data structure for creating a new user.
- UserLogin: A Pydantic model defining the data structure for user login.
"""

from pydantic import BaseModel

class UserCreate(BaseModel):
    """
    A Pydantic model that defines the data structure for creating a new user.
    
    Attributes:
    - username (str): The username of the new user.
    - password (str): The password for the new user.
    """
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    confirmPassword: str

class UserLogin(BaseModel):
    """
    A Pydantic model that defines the data structure for user login.
    
    Attributes:
    - username (str): The username used for login.
    - password (str): The password used for login.
    """
    username: str
    password: str

class UserOut(BaseModel):
    """
    A Pydantic model that defines the data structure for user output.
    
    Attributes:
    - username (str): The username of the user.
    """
    username: str

class Token(BaseModel):
    """
    A Pydantic model that defines the data structure for a JWT token.
    
    Attributes:
    - access_token (str): The access token.
    - token_type (str): The token type.
    """
    access_token: str
    token_type: str

