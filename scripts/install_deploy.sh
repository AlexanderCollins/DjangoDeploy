#!/bin/bash
sudo apt-get install nginx gunicorn -y

# gunicorn configuration
sudo touch /etc/systemd/system/gunicorn.service
sudo touch /etc/systemd/system/gunicorn.conf
sudo touch /etc/systemd/system/gunicorn.socket

sudo echo "
d /run/gunicorn 0755 $1 sudo -
" > /etc/systemd/system/gunicorn.conf

sudo echo "
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn/socket

[Install]
WantedBy=sockets.target
" > /etc/systemd/system/gunicorn.socket

sudo echo "
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
PIDFile=/run/gunicorn/pid
User=root
Group=sudo
RuntimeDirectory=/home/$1/env/bin/gunicorn
WorkingDirectory=/home/$1/$2
ExecStart=/home/$1/env/bin/gunicorn --pid /run/gunicorn/pid   \
          --bind unix:/home/$1/$2/$3.sock $3.wsgi   \
          --workers 3
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s TERM $MAINPID
PrivateTmp=true

[Install]
WantedBy=multi-user.target
" > /etc/systemd/system/gunicorn.service
sudo chmod 746 /etc/systemd/system/gunicorn.service

# start gunicorn service
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn


# start gunicon on startup
sudo update-rc.d gunicorn defaults

# nginx configuration
sudo touch /etc/nginx/sites-available/$2

sudo echo "
server {
    listen 80;
    server_name $(ifconfig | grep -A 1 'eth0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1);

    location = /favicon.ico { access_log off; log_not_found off; }

    location /api/ {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn/socket;
    }
}
" > /etc/nginx/sites-available/$2

sudo ln -s /etc/nginx/sites-available/$2 /etc/nginx/sites-enabled

sudo systemctl start nginx
sudo systemctl enable nginx

sudo systemctl restart nginx && sudo systemctl restart gunicorn
