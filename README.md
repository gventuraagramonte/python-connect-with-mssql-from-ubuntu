# python-connect-with-mssql-from-ubuntu
 This repository help to connect python to mssql server 2017 from ubuntu 18.04
 
 1. Install mssql in ubuntu 18.04
 
 $ sudo su
 $ sudo apt-get update
 $ sudo apt-get upgrade
 $ sudo reboot --> You need restart your pc.
 ...
 $ sudo su
 $ curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
 $ curl curl https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list | sudo tee /etc/apt/sources.list.d/mssql-server.list
 $ sudo apt-get update
 $ sudo apt-get install -y mssql-server
 $ sudo /opt/mssql/bin/sqlservr-setup
 
 2. If you want verified the installation, you can use the next command:
 $ systemctl status mssql-server.service
 
 
