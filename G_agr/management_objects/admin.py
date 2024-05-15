from django.contrib import admin

from .models import Reservation,visit


# Register your models here.

admin.site.register(Reservation)
admin.site.register(visit)