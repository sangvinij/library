#!/bin/bash
python project/manage.py migrate
python project/create_default_db_data.py
gunicorn -b 0.0.0.0:8000 project.project.wsgi:application
