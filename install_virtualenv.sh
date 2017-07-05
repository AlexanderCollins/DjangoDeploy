#!/bin/bash

echo "\n\napt-get install python3-pip -y\n\n"
sudo apt-get install python3-pip -y

echo "\n\nsudo pip3 install virtualenv\n\n"
sudo pip3 install virtualenv
cd /home/$1/

echo "\n\nvirtualenv --no-site-packages -p $(which python3) env\n\n"
virtualenv --no-site-packages -p $(which python3) env

# install mysql client
sudo /home/$1/env/bin/pip3 install mysqlclient
