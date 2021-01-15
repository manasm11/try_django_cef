from django.contrib import admin
from profiles_api import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Feed)