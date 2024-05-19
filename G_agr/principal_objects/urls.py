from django.contrib import admin
from django.urls import path, include 

from . import views


urlpatterns = [
    path("<str:account_id>/agriturismo/<str:funzione>/<str:filtro>", views.gestione_agtriturismi,name="gestione_agriturismi"),
    path("<str:account_id>/<str:agriturismo_id>/attivita/<str:funzione>/<str:filtro>", views.gestione_attivita,name="gestione_attivita"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/tipo_oggetti/<str:funzione>/<str:filtro>", views.gestione_tipo_oggetto,name="gestione_tipo_oggetto"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/<str:tipo_oggetti_id>/oggetto_singolo/<str:funzione>/<str:filtro>", views.gestione_oggetto_singolo,name="gestione_oggetto_singolo"),
]