#!/usr/bin/env bash
set -e
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
