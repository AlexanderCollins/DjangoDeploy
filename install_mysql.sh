#!/bin/bash

echo "mysql-server-5.7 mysql-server/root_password password $1" | sudo debconf-set-selections
echo "mysql-server-5.7 mysql-server/root_password_again password $1" | sudo debconf-set-selections
sudo apt-get -y install mysql-server-5.7

# Run the MySQL Secure Installation wizard - This code is equivalent to the provided mysql_secure_installation script.
# Make sure that NOBODY can access the server without a password
mysql -e "UPDATE mysql.user SET Password = PASSWORD('$1') WHERE User = 'root'" --password="$1"
# Kill the anonymous users
mysql -e "DROP USER ''@'localhost'" --password="$1"
# Because our hostname varies we'll use some Bash magic here.
mysql -e "DROP USER ''@'$(hostname)'" --password="$1"
# Kill off the demo database
mysql -e "DROP DATABASE test" --password="$1"
# create project database
mysql -e "CREATE DATABASE $2" --password="$1"
# Make our changes take effect
mysql -e "FLUSH PRIVILEGES" --password="$1"
# Any subsequent tries to run queries this way will get access denied because lack of usr/pwd param

service mysql restart
# run mysql service on boot
sudo update-rc.d mysql defaults
