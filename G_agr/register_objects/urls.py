from django.urls import path
from . import views

urlpatterns = [
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/entrate/<str:funzione>/<str:filtro>", views.gestione_entrate,name="gestione_entrate"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/uscite/<str:funzione>/<str:filtro>", views.gestione_uscite,name="gestione_uscite"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/clienti/<str:funzione>/<str:filtro>", views.gestione_clienti,name="gestione_clienti"),
    path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/lavoratori/<str:funzione>/<str:filtro>", views.gestione_lavoratori,name="gestione_lavoratori"),
    #path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/promozioni/<str:funzione>/<str:filtro>", views.gestione_promozioni,name="gestione_promozioni"),
    #path("<str:account_id>/<str:agriturismo_id>/<str:attivita_id>/servizzi/<str:funzione>/<str:filtro>", views.gestione_servizzi,name="gestione_servizzi"),
]