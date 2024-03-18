from django.contrib import admin

from .models import Question,Room,Choice,Clients,services,employee

admin.site.register(Question)
admin.site.register(Room)
admin.site.register(Choice)
admin.site.register(Clients)
admin.site.register(services)
admin.site.register(employee)