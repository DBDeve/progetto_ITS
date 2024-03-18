from django.urls import path

from . import views

#quando creo una pagina in view devo metterla qui 
urlpatterns = [
    path("", views.index, name="index"),
    path("pagina", views.pagina, name="pagina"),
    path("myfirst", views.myfirst, name="myfirst"),
    path("home", views.home, name="home"),
    path("camere", views.camere, name="camere"),

    # path("nome_template",views.nome_template, name="nome_nome_template")
    #scaricare bootstrap
    #andare sui creatori di template per bootstrap

    ]

