from django.contrib import admin

# Register your models here.

from .models import Services,Employee,AccountManagers,Earnings,FarmHouses,Expense,Salary,Clients




admin.site.register(Services)
admin.site.register(Employee)
admin.site.register(AccountManagers)
admin.site.register(Earnings)
admin.site.register(FarmHouses)
admin.site.register(Expense)
admin.site.register(Salary)
admin.site.register(Clients)

