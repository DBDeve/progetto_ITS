from django.urls import path
from . import views

urlpatterns = [
    path("cambia_password",views.cambia_password,name="cambia_password"),
    path("registrati", views.registrati,name="registrati"),
    path("login",views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
]