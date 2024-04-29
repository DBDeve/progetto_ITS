from django.contrib import admin
from django.urls import path, include 

from . import views

#quando creo una pagina in view devo metterla qui 
urlpatterns = [

    path("visualizza/<str:username>/<str:agriturismo>/<str:argomento>/<str:scelta>", views.visualizza, name="visualizza"),
    path("visualizza/<str:username>/tutti/<str:argomento>/<str:scelta>", views.visualizza, name="visualizza"),

    path("<str:username>/<str:agriturismo>/aggiungi/<str:argomento>", views.aggiungi, name="aggiungi"),

    path("elimina/<str:username>/<str:agriturismo>/<str:argomento>/<str:valore>", views.elimina, name="elimina"),
    
    path("modifica/<str:username>/<str:agriturismo>/<str:argomento>", views.modifica, name="modifica"),
    path("modifica/<str:username>/<str:agriturismo>/<str:argomento>/<str:valore>", views.modifica, name="modifica"),
    
    path("<str:username>/<str:agriturismo>/prenotazioni/<str:funzione>/<str:filtro>", views.prenotazioni, name="prenotazioni"),

    path("<str:username>/aggiungi/agriturismo", views.verifica_aggiungi_agtriturismo,name="aggiungi agriturismo"),
    path("cambia_password",views.cambia_password,name="cambia_password"),
    path("registrati", views.registrati,name="registrati"),
    path("login",views.accedi, name="login"),
    path("logout", views.log_out, name="logout")

    # path("nome_template",views.nome_template, name="nome_nome_template")
    #scaricare bootstrap
    #andare sui creatori di template per bootstrap

    ]

