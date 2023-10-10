# Print a message to check if the script is executed
echo "Start executing build_files.sh script"


# Collect static files
python manage.py collectstatic --noinput

echo "End executing build_files.sh script"
