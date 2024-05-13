"""
URL configuration for G_agr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#serve ad includere tutti gli altri def in view
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('system/',include('system.urls')),
    path('principal_objects/',include('principal_objects.urls')),
    path('management_objects/',include('management_objects.urls')),
    path('register_objects/',include('registrer_objects.urls')),
    path('view/',include('view.urls')),
]
