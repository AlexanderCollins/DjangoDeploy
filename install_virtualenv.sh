#!/bin/bash

sudo apt-get install python3-pip -y
sudo pip3 install virtualenv

cd ~/
virtualenv --no-site-packages -p $(which python3) env

# install mysql client
sudo su
~/env/bin/pip3 install mysqlclient
exit
