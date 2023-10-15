"""
core/db_config.py

This module is responsible for managing the configuration settings related to the database. It utilizes Pydantic's 
BaseSettings to facilitate environment variable management and type validation. Additionally, it employs python-dotenv 
to load environment variables from a file.

Classes:
- DBConfig: Manages database configuration settings and constructs the SQLAlchemy database URI.

Functions:
- load_dotenv: Loads environment variables from a specified file into the system environment.

Variables:
- POSTGRES_USER: The username used to authenticate with the PostgreSQL database.
- POSTGRES_PASSWORD: The password used to authenticate with the PostgreSQL database.
- POSTGRES_HOST: The host of the PostgreSQL database.
- POSTGRES_DB: The name of the PostgreSQL database to connect to.
- SQLALCHEMY_DATABASE_URI: The full URI used by SQLAlchemy to connect to the database.

Methods:
- sqlalchemy_database_uri: Constructs the SQLAlchemy database URI using the provided database settings.
"""

from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from the specified file.
load_dotenv("environments/db.env")

class DBConfig(BaseSettings):
    """
    A class used to manage database configuration settings. Inherits from Pydantic's BaseSettings to leverage 
    environment variable management and type validation.
    uri format = postgresql://user:password@host:port/dbname
    
    Attributes:
    - POSTGRES_USER (str): Username for PostgreSQL authentication.
    - POSTGRES_PASSWORD (SecretStr): Password for PostgreSQL authentication.
    - POSTGRES_HOST (str): Host address of the PostgreSQL database.
    - POSTGRES_DB (str): Name of the PostgreSQL database to connect to.
    - SQLALCHEMY_DATABASE_URI (PostgresDsn, optional): Full URI for SQLAlchemy database connection.
    
    Methods:
    - sqlalchemy_database_uri(self) -> str: Constructs and returns the SQLAlchemy database URI.
    """
    
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: str
    POSTGRES_DB: str

    SQLALCHEMY_DATABASE_URI: PostgresDsn = "postgresql://none:none@none:5432/none"

    class Config:
        # Specify the file path for environment variables.
        env_file = "environments/db.env"

    @property
    def sqlalchemy_database_uri(self) -> str:
        """
        Constructs the SQLAlchemy database URI using the provided database settings.
        
        Returns:
        - str: The constructed SQLAlchemy database URI.
        """
        uri: PostgresDsn = f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD.get_secret_value()}@{self.POSTGRES_HOST}/{self.POSTGRES_DB}"

        return uri
        