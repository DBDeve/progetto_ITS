from django.urls import path
from . import views

urlpatterns = [
    path("<str:account_id>/<str:gruppo_oggetti_id>/prenotazioni/<str:funzione>/<str:prenotazione_id>", views.gestione_prenotazioni,name="gestione_prenotazioni"),   
]