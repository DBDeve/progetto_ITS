from django.contrib import admin

from .models import Earnings,Expense,Employee,Clients,Services,Promotions

# Register your models here.

admin.site.register(Earnings)
admin.site.register(Expense)
admin.site.register(Employee)
admin.site.register(Clients)
admin.site.register(Services)
admin.site.register(Promotions)




