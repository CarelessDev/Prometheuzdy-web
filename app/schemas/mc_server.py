from pydantic import BaseModel 

class MCServerInfo(BaseModel):
    """
    A Pydantic model that defines the data structure for server information.
    
    Attributes:
    - id (int): The unique identifier for a server, primary key.
    - server_name (str): The name of the Minecraft server.
    - server_ip (str): The IP address of the Minecraft server.
    - server_port (int): The port number of the Minecraft server.
    - server_version (str): The version of the Minecraft server.
    - server_execute_cmd (str): The path or name of the server's executable file.
    """
    id: int
    server_name: str
    server_ip: str
    server_port: int
    server_version: str
    server_execute_cmd: str
    server_note: str
    ssh_username: str
    ssh_port: int
    ssh_public_key: str


class MCServerInitiateResponse(BaseModel):
    stdout: str
    stderr: str


class MCServerTerminateResponse(BaseModel):
    stdout: str
    stderr: str
