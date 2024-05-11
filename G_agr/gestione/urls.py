from django.contrib import admin
from django.urls import path, include 

from . import views

#quando creo una pagina in view devo metterla qui 
urlpatterns = [

    #url di sistema
    path("cambia_password",views.cambia_password,name="cambia_password"),
    path("registrati", views.registrati,name="registrati"),
    path("login",views.accedi, name="login"),
    path("logout", views.log_out, name="logout"),

    path("<str:username>/agriturismo/<str:funzione>/<str:filtro>", views.gestione_agtriturismi,name="gestione_agriturismi"),
    path("<str:username>/<str:agriturismo>/attivita/<str:funzione>/<str:filtro>", views.gestione_attivita,name="gestione_attivita"),
    path("<str:username>/<str:agriturismo>/<str:attivita>/gruppo_oggetti/<str:funzione>/<str:filtro>", views.gestione_oggetti,name="gestione_oggetti"),



 
    #url per oggetti generici
    path("<str:username>/<str:agriturismo>/<str:oggetto>/aggiungi", views.aggiungi, name="aggiungi"),
    path("<str:username>/<str:agriturismo>/<str:oggetto>/elimina/<str:id_oggetto>", views.elimina, name="elimina"),
    path("<str:username>/<str:agriturismo>/<str:oggetto>/modifica/<str:id_oggetto>", views.modifica, name="modifica"),

    path("<str:username>/<str:agriturismo>/<str:oggetto>/visualizza/<str:filtro>", views.visualizza, name="visualizza"),
    path("<str:username>/tutti/<str:oggetto>/visualizza/<str:filtro>", views.visualizza, name="visualizza"),

    
    #url per oggetti specifici
    #path("<str:username>/<str:agriturismo>/prenotazioni/<str:attivita>/<str:funzione>/<str:filtro>", views.gestione_prenotazioni, name="prenotazioni"),
    #path("<str:username>/<str:agriturismo>/gestione_clienti_presenti/<str:funzione>/<str:filtro>", views.gestione_clienti_presenti, name="gestione_clienti_presenti"),

    ]  