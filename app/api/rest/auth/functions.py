from passlib.context import CryptContext


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
