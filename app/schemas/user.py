"""
app/schemas/user.py

This module defines Pydantic models for user information management within the application. These models are utilized 
to validate and structure the data payload in HTTP responses related to user information retrieval.

Classes:
- UserInfo: A Pydantic model defining the data structure for user information.
"""

from pydantic import BaseModel 

class UserInfo(BaseModel):
    """
    A Pydantic model that defines the data structure for user information.
    
    Attributes:
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.
    - username (str): The username of the user.
    - email (str): The email address of the user.
    """
    first_name: str
    last_name: str
    username: str
    email: str
