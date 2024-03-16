from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.customUser)
admin.site.register(models.posts)