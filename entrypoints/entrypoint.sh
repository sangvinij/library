#!/bin/bash
python project/manage.py migrate
python project/create_default_db_data.py
python project/manage.py runserver
