from django.contrib import admin
from django.urls import path, include 

from . import views

#quando creo una pagina in view devo metterla qui 
urlpatterns = [
    #path("<str:username>/visualizza/<str:argomento>/<str:scelta>", views.visualizza, name="visualizza"),
    path("visualizza/<str:username>/<str:argomento>/<str:scelta>", views.visualizza, name="visualizza"),
    

    path("aggiungi/<str:username>/<str:argomento>", views.aggiungi, name="aggiungi"),
    path("elimina/<str:username>/<str:argomento>", views.elimina, name="elimina"),
    
    #path per la funzione modifica
    #path("modifica/<str:argomento>", views.modifica, name="modifica"),
    path("modifica/<str:username>/<str:argomento>", views.modifica, name="modifica"),
    #path("accounts/", include("django.contrib.auth.urls")),  # Include le viste di autenticazione
    path("registrati", views.registrati,name="registrati"),
    path("login",views.accedi, name="login"),
    path("logout", views.log_out, name="logout")

    # path("nome_template",views.nome_template, name="nome_nome_template")
    #scaricare bootstrap
    #andare sui creatori di template per bootstrap

    ]

