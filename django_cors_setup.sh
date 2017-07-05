#!/bin/bash
serveripaddress=$(ifconfig | grep -A 1 "eth0" | tail -1 | cut -d ":" -f 2 | cut -d " " -f 1)
sudo sed -i 's/SERVERIPADDRESS/'"$serveripaddress"'/g' ~/$1/$2/settings.py
sudo echo "
prefix = '$serveripaddress'
" >> ~/$1/$2/settings.py
