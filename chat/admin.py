from django.contrib import admin

# Register your models here.
#chat/admin.py

from .models import *
# Register your models here.

admin.site.register(Message)
admin.site.register(Event)
admin.site.register(Group)