#!/bin/bash
sudo apt-get install python3-pip -y
sudo pip3 install virtualenv
cd /home/$1/
virtualenv --no-site-packages -p $(which python3) env

# install mysql client
sudo /home/$1/env/bin/pip3 install mysqlclient

# install gunicorn
sudo /home/$1/env/bin/pip3 install gunicorn

