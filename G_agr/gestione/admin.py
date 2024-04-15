from django.contrib import admin

# Register your models here.

from .models import Rooms,Services,Employee,AccountManagers,Earnings,FarmHouses,GoOut,Salary,Clients



admin.site.register(Rooms)
admin.site.register(Services)
admin.site.register(Employee)
admin.site.register(AccountManagers)
admin.site.register(Earnings)
admin.site.register(FarmHouses)
admin.site.register(GoOut)
admin.site.register(Salary)
admin.site.register(Clients)

