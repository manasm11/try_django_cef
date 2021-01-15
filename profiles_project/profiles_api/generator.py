#!/usr/bin/env python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "profiles_project.settings")

# your imports, e.g. Django models
# from profiles_project.models import User
from . import models
from django.utils import timezone

users = [
    {
        'email':'f20170546@pilani.bits-pilani.ac.in',
        'name':'Manas Mishra',
        'password':'testing321'
    },
    {
        'email':'f20170727@pilani.bits-pilani.ac.in',
        'name':'Divya Tyagi',
        'password':'testing321'
    },
    {
        'email':'f20170630@pilani.bits-pilani.ac.in',
        'name':'Lakshya',
        'password':'testing321'
    },
    {
        'email':'f20170531@pilani.bits-pilani.ac.in',
        'name':'Adya Pathak',
        'password':'testing321'
    },
    {
        'email':'f20170123@pilani.bits-pilani.ac.in',
        'name':'Hritik Something',
        'password':'testing321'
    },
]

feeds = [
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
    {
        'user':models.User.objects.get(id=1),
        'text':'Feed1 by user 1',
        'created_on':timezone.now(),
    },
]

def create_users():
    for user in users:
        models.User.objects.create_user(**user)

def create_feeds():
    for feed in feeds:
        models.Feed.objects.create(**feed)