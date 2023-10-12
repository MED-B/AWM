# myapp/management/commands/add_line_to_index.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Add a line to the index file'

    def handle(self, *args, **kwargs):
        file_path = 'path/to/jazzmin/templates/admin/index.html'
        new_line = "{% include 'dashboard_stats.html' %}\n"

        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Insert the new line after line 17
        lines.insert(17, new_line)

        with open(file_path, 'w') as file:
            file.writelines(lines)

        self.stdout.write(self.style.SUCCESS('Successfully added a line to index.html.'))
