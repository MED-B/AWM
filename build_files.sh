#!/bin/bash

# Assuming your Django project is in the AWM directory
cd AWM

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
