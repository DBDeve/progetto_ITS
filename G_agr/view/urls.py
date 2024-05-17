from django.urls import path
from . import views


urlpatterns = [
    path("<str:username>/<str:agriturismo>/<str:filtro>", views.visualizza_per_agriturismo,name="visualizza_per_agriturismo"),
    path("<str:username>/<str:agriturismo>/<str:attivita>/<str:filtro>", views.visualizza_per_attivita,name="visualizza_per_attivita"),
    path("<str:username>/<str:agriturismo>/<str:attivita>/<str:tipo_attivita>/<str:filtro>", views.visualizza_per_tipo_oggetto,name="visualizza_tipo_attivita"),
]