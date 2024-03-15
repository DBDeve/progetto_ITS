from django.contrib import admin

from models import (Member,room,services,Clients,employee,promotions)

# Register your models here.

admin.site.register(Member)
admin.site.register(room)
admin.site.register(services)
admin.site.register(Clients)
admin.site.register(employee)
admin.site.register(promotions)