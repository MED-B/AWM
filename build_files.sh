# Print a message to check if the script is executed
echo "Start executing build_files.sh script"

# !/bin/bash
# Set MySQL client environment variables
export MYSQLCLIENT_CFLAGS=""
export MYSQLCLIENT_LDFLAGS="" 

# Assuming your Django project is in the AWM directory
cd AWM

# Install dependencies
# pip install -r requirements.txt 

# Install mysqlclient manually
pip install mysqlclient

# Collect static files
python manage.py collectstatic --noinput

echo "End executing build_files.sh script"
