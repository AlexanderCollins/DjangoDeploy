#!/bin/bash

#set permissions
cd ~/djangodeploy
chmod +x set_permissions.sh
sudo ./set_permissions.sh

# setup ssh
mkdir ~/.ssh
chmod 700 ~/.ssh

#update
sudo ./update.sh

# --------- install software and deploy ---------

#install pre requisites
sudo ./install_pre_reqs.sh

# enable firewall open port 80
sudo ./raise_firewall.sh

# setup sql
sudo ./install_mysql.sh

# setup redis
sudo ./install_redis.sh

# install node
sudo ./install_node.sh

# install virtualenv
sudo ./install_virtualenv.sh

# --------- django build ---------

# install python libraries
sudo ./install_django_project.sh

# django setup database backend
sudo ./django_setup_mysql.sh

# django migrate
sudo ./django_migrate.sh

# django cors setup
sudo ./django_cors_setup.sh

# deploy
sudo ./install_deploy.sh $1

# status report
sudo ./status_report.sh
