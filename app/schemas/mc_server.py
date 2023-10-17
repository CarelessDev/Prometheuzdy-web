from pydantic import BaseModel 

class MCServerInfo(BaseModel):
    """
    A Pydantic model that defines the data structure for server information.
    
    Attributes:
    - server_name (str): The name of the Minecraft server.
    - server_ip (str): The IP address of the Minecraft server.
    - server_port (int): The port number of the Minecraft server.
    - server_version (str): The version of the Minecraft server.
    - server_executable (str): The path or name of the server's executable file.
    """
    server_name: str
    server_ip: str
    server_port: int
    server_version: str
    server_executable: str
    server_note: str
    ssh_username: str
    ssh_port: int


