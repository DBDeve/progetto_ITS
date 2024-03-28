from django.urls import path

from . import views

#quando creo una pagina in view devo metterla qui 
urlpatterns = [
    path("visualizza/<str:argomento>/<str:scelta>", views.visualizza, name="visualizza"),

    path("aggiungi/<str:argomento>", views.aggiungi, name="aggiungi"),
    path("elimina/<str:argomento>", views.elimina, name="elimina"),
    
    #path per la funzione modifica
    #path("modifica/<str:argomento>", views.modifica, name="modifica"),
    path("modifica/<str:argomento>/<str:valore_oggetto>", views.modifica, name="modifica"),

    

    # path("nome_template",views.nome_template, name="nome_nome_template")
    #scaricare bootstrap
    #andare sui creatori di template per bootstrap

    ]

