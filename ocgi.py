r"""
One Command Git init
init Git repository at local folder and over remote server using ssh.
Saves trouble of going to remote and creting directories manually.

Copyright 2017 - Sameer Bobade

MIT license

Credits: Paramiko for ssh client. http://www.paramiko.org/
==============================================================================

ABOUT & HOW TO USE
Tested on Windows 10 and Git server on Raspbian Jessie.

Run command in current folder to make it a git repository.
On server repository will be created in -
server/parent directory/working directory

Needs OpenSSH public / private key pair.
Key pair can be store in ~/.ssh directory.
On Windows this is C:\Users\<username>
Git on Windows uses cmd

Written in one file to ease copying the script.

Copy to Python script directory and run with "python -m ocgi"
e.g. C:\Program Files\Python35\Scripts
"""

import os
import subprocess
import socket

import paramiko

# Server configuration
HOST = "raspione.local"
PORT = 22
USER = "pi"
GIT_ROOT = "/media/pi/GitRepo"
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
GIT_ADD_REMOTE = "git remote add RasPiOne " + "ssh://" \
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
    print("Created repository directory")
    SSH.exec_command(CD + GIT_ROOT + WORK_DIR + THEN + GIT_INIT_BARE)
    print("Created bare Git repository")
    SSH.exec_command(LOGOUT)
    print("Logged out")
except paramiko.SSHException:
    print("Error - Server failed executing command")


SSH.close()
print("SSH session closed")


# Initialize local working directory as Git repository
try:
    subprocess.check_call(GIT_INIT, cwd=CWD)
    print("Git repository created in local working directory")
    subprocess.check_call(GIT_ADD_REMOTE, cwd=CWD)
    print("Added Git remote")
    subprocess.check_call(GIT_FETCH, cwd=CWD)
    print("Git Fetch")
except OSError:
    print("Local git creation failed")
except subprocess.CalledProcessError:
    print("Remote with same name already exists.")

print("Done")
