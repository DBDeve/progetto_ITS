from django.urls import path
from . import views


urlpatterns = [
    #path("<str:username>/<str:agriturismo_id>", views.visualizza_per_agriturismo,name="visualizza_per_agriturismo"),

    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/<str:lista>", views.visualizza_per_attivita,name="visualizza_per_attivita"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/entrate", views.visualizza_per_attivita,name="visualizza_per_attivita"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/uscite", views.visualizza_per_attivita,name="visualizza_per_attivita"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/lavoratori", views.visualizza_per_attivita,name="visualizza_per_attivita"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/clienti", views.visualizza_per_attivita,name="visualizza_per_attivita"),

    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/<str:gruppo_oggetti_id>/<str:filtro>", views.visualizza_per_gruppi_oggetti,name="visualizza_tipo_attivita"),
]