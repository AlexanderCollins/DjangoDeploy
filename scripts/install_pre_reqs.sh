#!/bin/bash

#install prereqs
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install build-essential git htop -y
sudo apt-get install python3-dev libmysqlclient-dev -y
