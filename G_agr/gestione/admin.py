from django.contrib import admin

# Register your models here.

from .models import Room,services,employee



admin.site.register(Room)
admin.site.register(services)
admin.site.register(employee)

