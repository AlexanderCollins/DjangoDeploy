#!/bin/bash

source ~/env/bin/activate
python ~/$1/manage.py makemigrations
python ~/$1/manage.py migrate
