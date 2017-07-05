#!/bin/bash

# enable firewall and open port 80
echo 'y' | ufw enable
ufw allow 80

# open port for websockets
ufw allow 8080

# open port 22 for ssh
ufw allow 22


