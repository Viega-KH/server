from django.contrib import admin
from .models import contactlink
# Register your models here.
from django.contrib.auth.models import User, Group

# User va Group modellarini admin paneldan olib tashlash
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(contactlink)