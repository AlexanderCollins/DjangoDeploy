#!/bin/bash

echo "
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 'mysql.connector.django',  # alternative (pure python, use with gevent)
        'NAME': '$4',
        'USER': 'root',
        'PASSWORD': '$3',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4', 'init_command': \"SET sql_mode='STRICT_TRANS_TABLES'\"},
    }
}
" >> ~/$1/$2/settings.py
