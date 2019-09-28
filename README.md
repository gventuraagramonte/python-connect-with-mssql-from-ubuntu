# python-connect-with-mssql-from-ubuntu
 This repository help to connect python to mssql server 2017 from ubuntu 18.04
 
 1. Install mssql in ubuntu 18.04
 
 <p>$ sudo su</p>
 <p>$ sudo apt-get update</p>
 <p>$ sudo apt-get upgrade</p>
 <p>$ sudo reboot</p> --> You need restart your pc.
 ...
 <p>$ sudo su</p>
 <p>$ curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -</p>
 <p>$ curl curl https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list | sudo tee /etc/apt/sources.list.d/mssql-server.list</p>
 <p>$ sudo apt-get update</p>
 <p>$ sudo apt-get install -y mssql-server</p>
 <p>$ sudo /opt/mssql/bin/sqlservr-setup</p>
 
 <p>2. If you want verified the installation, you can use the next command:</p>
 <p>$ systemctl status mssql-server.service</p>
 <a href="C:\Users\Computer\Downloads\1.PNG">Visit W3Schools</a>
 
