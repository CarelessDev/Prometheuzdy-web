from fastapi import Depends
from app.db.session import get_db
from app.models.mc_server import MCServer
from app.schemas.mc_server import MCServerTerminateResponse
from sqlalchemy.orm import Session

import os
from io import StringIO

import paramiko

def stop_minecraft_server(server_id: int, db: Session = Depends(get_db)) -> MCServerTerminateResponse:
    """
    Stop a minecraft server by server_id.
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

    cmd = server_info.stop_cmd

    _, stdout, stderr = client.exec_command(cmd)

    # Close the connection
    client.close()


    return MCServerTerminateResponse(stdout=stdout.read().decode(), stderr=stderr.read().decode()) 