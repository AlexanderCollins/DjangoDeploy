#!/bin/bash

# satisfy requirements
sudo apt-get install tcl8.5 -y

# download and install redis
cd ~/
wget http://download.redis.io/releases/redis-stable.tar.gz
tar xzf redis-stable.tar.gz
cd redis-stable
make
#make test
sudo make install

# run as background process
cd utils
echo -n | ./install_server.sh

# set redis to run at boot
sudo update-rc.d redis_6379 defaults
cd ~/haver_deploy
