#!/bin/bash

# set the time zone of the server
sudo timedatectl set-timezone UTC
sudo apt-get install language-pack-en -y
sudo apt-get update && sudo apt-get upgrade -y
