"""
PLACE THIS FILE INSIDE VIRTUAL ENVIRONMENT
'dj3/lib/python3.8/site-packages/django/core/management/commands/setup_app.py'
"""
from django.core.management.base import BaseCommand
import os

def check(condition, message="Error occured"):
    if not condition: print(message) and exit()

class Command(BaseCommand):
    help = "Clears terminal !!!"

    def handle(self, **options):
        app_name = input("Enter app name > ")
        os.system(f"./manage.py startapp {app_name}")
        os.makedirs(f"{app_name}/templates/{app_name}")
        project_name = open("manage.py").read().split("'")[4].split(".")[0]
        os.system(f"cp -u {project_name}/urls.py {app_name}/urls.py")
        os.system(f"cd {app_name}/templates/{app_name} && touch base.html index.html")
        # os.system(f"touch {app_name}/forms.py {app_name}/serializers.py")
