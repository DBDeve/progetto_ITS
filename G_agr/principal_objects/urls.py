from django.contrib import admin
from django.urls import path, include 

from . import views


urlpatterns = [
    path("<str:username>/agriturismo/<str:funzione>/<str:filtro>", views.gestione_agtriturismi,name="gestione_agriturismi"),
    path("<str:username>/<str:agriturismo>/attivita/<str:funzione>/<str:filtro>", views.gestione_attivita,name="gestione_attivita"),
    path("<str:username>/<str:agriturismo>/<str:attivita>/tipo_oggetti/<str:funzione>/<str:filtro>", views.gestione_tipo_oggetto,name="gestione_tipo_oggetto"),
    path("<str:username>/<str:agriturismo>/<str:attivita>/<str:tipo_oggetti>/oggetto_singolo/<str:funzione>/<str:filtro>", views.gestione_oggetto_singolo,name="gestione_oggetto_singolo"),
]