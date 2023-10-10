# Print a message to check if the script is executed
echo "Start executing build_files.sh script"

# Set MySQL client environment variables
export MYSQLCLIENT_CFLAGS=""
export MYSQLCLIENT_LDFLAGS=""

# Print current working directory
echo "Current directory: $(pwd)"

# List contents of the current directory
echo "Directory contents: $(ls)"

# Get the current working directory
CURRENT_DIR=$(pwd)

# List contents of the current directory
echo "Directory contents: $(ls)"
# Install dependencies
pip install -r requirements.txt

# Install mysqlclient manually
pip install mysqlclient

# Collect static files
python manage.py collectstatic --noinput

echo "End executing build_files.sh script"
