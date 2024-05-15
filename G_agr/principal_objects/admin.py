from django.contrib import admin

from .models import AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject

admin.site.register(AccountManagers)
admin.site.register(FarmHouses)
admin.site.register(Activity)
admin.site.register(TypeObjects)
admin.site.register(ActivityObject)

# Register your models here.
