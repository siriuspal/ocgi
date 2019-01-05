"""
One Command Git init
init Git repository at local folder and over remote server using ssh.
Saves trouble of going to remote and to create directories manually.

Copyright 2017 - Sameer Bobade

MIT license
"""

__author__ = "Sameer Bobade - www.siriuspal.com"
__copyright__ = "Copyright 2017 - Sameer Bobade"
__credits__ = ["Paramiko - http://www.paramiko.org/"]
__license__ = "MIT license"
__version__ = "0.1.1"

import os
import subprocess
import socket

import paramiko

# Server configuration
HOST = "<localhost>"
PORT = 22
USER = "<user>"
GIT_ROOT = "<repository root dir>"

GIT_INIT_BARE = "sudo git init --bare"
GIT_FETCH = "git fetch --all"
THEN = ";"
LOGOUT = "logout"
MKDIR = "mkdir "
CD = "cd "

# Get working and parent directory
CWD = os.getcwd()
# Maybe Windows specific implementation
SPLIT_DIR = CWD.split("\\")
PAR_DIR = "/" + SPLIT_DIR[-2]
WORK_DIR = PAR_DIR + "/" + SPLIT_DIR[-1]

# Windows Configuration
GIT_INIT = "git init"
GIT_ADD_REMOTE = "git remote add Origin " + "ssh://" \
    + USER + "@" + HOST + ":" + GIT_ROOT + WORK_DIR


# Connect to server
try:
    SSH = paramiko.SSHClient()
    SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SSH.connect(HOST, port=PORT, username=USER, look_for_keys=True)
    print("Connected to remote server")
except paramiko.BadHostKeyException:
    print("Bad key. Server's host key could not be verified")
except paramiko.AuthenticationException:
    print("Authentication failure")
except paramiko.SSHException:
    print("Error establishing an SSH session")
except socket.error:
    print("Socket error occured while connecting")

# Create directories and init git
try:
    SSH.exec_command(MKDIR + GIT_ROOT + PAR_DIR)
    SSH.exec_command(MKDIR + GIT_ROOT + WORK_DIR)
    stdin, stdout, stderr = SSH.exec_command(
        CD + GIT_ROOT + WORK_DIR + THEN + GIT_INIT_BARE)
    print(str(stdout.readlines()[0]))
    SSH.exec_command(LOGOUT)
except paramiko.SSHException:
    print("Error - Server failed executing command")


SSH.close()
print("SSH session closed")


# Initialize local working directory as Git repository
try:
    subprocess.check_call(GIT_INIT, cwd=CWD)
    subprocess.check_call(GIT_ADD_REMOTE, cwd=CWD)
    print("Added Git remote")
    subprocess.check_call(GIT_FETCH, cwd=CWD)
except OSError:
    print("Local git creation failed")
except subprocess.CalledProcessError:
    print("Remote with same name already exists.")

print("Done")
