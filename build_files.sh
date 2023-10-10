# Print a message to check if the script is executed
echo "Start executing build_files.sh script"

# !/bin/bash
# Set MySQL client environment variables
export MYSQLCLIENT_CFLAGS=""
export MYSQLCLIENT_LDFLAGS="" 

# Print current working directory
echo "Current directory: $(pwd)"

# List contents of the current directory
echo "Directory contents: $(ls)"

# Assuming your Django project is in the AWM directory
cd AWM

# List contents of the current directory
echo "Directory contents: $(ls)" 

# Install dependencies
pip install -r AWM/requirements.txt 

# Install mysqlclient manually
pip install mysqlclient

# Collect static files
python manage.py collectstatic --noinput

echo "End executing build_files.sh script"
