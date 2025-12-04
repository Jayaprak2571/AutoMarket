#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Userservice.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()




'''

from django.db import connection
with connection.cursor() as cursor:
...     cursor.execute("SELECT name from sqlite_master WHERE type='table';")
...     print("Tables ",cursor.fetchall())
...
<django.db.backends.sqlite3.base.SQLiteCursorWrapper object at 0x0000028481A3E560>
Tables  [('django_migrations',), ('sqlite_sequence',), ('Cars_car',), ('Cars_carimage',), ('auth_group_permissions',), ('auth_user_groups',), ('auth_user_user_permissions',), ('django_admin_log',), ('django_content_type',), ('auth_permission',), ('auth_group',), ('auth_user',), ('django_session',)]
with connection.cursor() as cursor:
...     cursor.execute("UPDATE sqlite_sequence SET seq = 3999 WHERE name='Cars_car';")
...
<django.db.backends.sqlite3.base.SQLiteCursorWrapper object at 0x0000028481A3E5F0>
'''