#ocgi

One command git init for repository on private server

ABOUT & HOW TO USE

Run "python -m ocgi" command in current folder to make it a git repository. On server repository will be created in - server/parent directory/working directory

Needs OpenSSH public / private key pair. Key pair can be store in ~/.ssh directory. 

Written in one file to ease copying the script.

Add to Python path by creating <package>.pth and add it to
<installation dir>\Python35\Lib\site-packages
OR directly copy this script to <installation dir>\Python35\Lib\site-packages

Tested on Windows 10 and Git server on Raspbian Jessie. On Windows this is C:\Users\<username>. Git on Windows uses cmd
