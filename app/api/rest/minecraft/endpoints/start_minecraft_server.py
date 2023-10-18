from fastapi import Depends
from app.db.session import get_db
from app.models.mc_server import MCServer
from app.schemas.mc_server import MCServerInitiateResponse
from sqlalchemy.orm import Session

import os
from io import StringIO

import paramiko

def start_minecraft_server(server_id: int, db: Session = Depends(get_db)) -> MCServerInitiateResponse:
    """
    Start a minecraft server by server_id.
    """
    server_info = db.query(MCServer).filter(MCServer.id == server_id).first()


    # Establish SSH connection
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    private_key = paramiko.RSAKey(file_obj=StringIO(os.environ.get("SSH_KEY")))

    # Connect to the server
    client.connect(
        hostname=server_info.server_ip,
        port=server_info.ssh_port,
        username=server_info.ssh_username,
        pkey=private_key
    )

    cmd = server_info.start_cmd

    _, stdout, stderr = client.exec_command(cmd)

    # Close the connection
    client.close()


    return MCServerInitiateResponse(stdout=stdout.read().decode(), stderr=stderr.read().decode()) 