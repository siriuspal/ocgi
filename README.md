#ocgi

One command git init for git repository on private server. Written in Python.    

I wrote this because I was not able to initialize remote repository without manually creating directories on server.

ABOUT & HOW TO USE

Run "python -m ocgi" command in current folder to make it a git repository. On server repository will be created in - server/repository root/parent directory/working directory

Needs OpenSSH public / private key pair. Key pair can be store in ~/.ssh directory. On Windows 10 this is C:\Users\<username>.       

Add to Python path by creating <package>.pth and add it to
<installation dir>\Python35\Lib\site-packages
OR directly copy this script to <installation dir>\Python35\Lib\site-packages

Tested on Windows 10 and Git server on Raspbian Jessie. Git on Windows Shell. 
