from django.urls import path

from . import views

#quando creo una pagina in view devo metterla qui 
urlpatterns = [
    path("", views.index, name="index"),
    path("pagina", views.pagina, name="pagina"),
    path("myfirst", views.myfirst, name="myfirst"),
    ]

