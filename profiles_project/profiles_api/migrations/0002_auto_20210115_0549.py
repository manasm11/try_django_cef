# Generated by Django 3.1.4 on 2021-01-15 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeedItem',
            new_name='Feed',
        ),
    ]