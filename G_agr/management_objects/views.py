from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from django.template import loader

from .models import AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject
from .models import Clients
from .models import Reservation

# Create your views here.

@login_required(login_url='login')
def gestione_prenotazioni(request,account_id, gruppo_oggetti_id, funzione, prenotazione_id):
    context={}
    
    #memorizza il tipo della funzione
    context['funzione']=funzione

    #prende il tipo di oggetto selezionato
    gruppo=TypeObjects.objects.get(id=gruppo_oggetti_id)
    context['gruppo_name']=gruppo
    context['gruppo_id']=gruppo_oggetti_id

    #crea una lista di tutti i clenti dell'account
    context['lista_clienti_occount']=Clients.objects.filter(IdAccountManagers=account_id)

    #crea una lista di tutti gli oggetti di un certo gruppo
    context['lista_oggetti_gruppo']=ActivityObject.objects.filter(IdTypeObjects=gruppo_oggetti_id)

    if funzione=="aggiungi":
        if request.POST:
         id_oggetto=request.POST['camera_id']
         oggetto=ActivityObject.objects.get(id=id_oggetto)
         oggetto.stato="prenotata"
         oggetto.save()

         id_cliente=request.POST['cliente_id']
         cliente=Clients.objects.get(id=id_cliente)
         cliente.stato="attuale"
         cliente.save()

         nuova_prenotazione=Reservation(
            IdTypeObjects=gruppo_oggetti_id,
            IdActivityObject=request.POST['camera_id'],
            IdClient=request.POST['cliente_id'],
            frOm_data=request.POST['data_arrivo'],
            to=request.POST['data_partenza']
         )
         nuova_prenotazione.save()

         return render(request, "visualizza_per_attivita.html", context)
      
    elif funzione=="elimina":
      prenotazione_da_eliminare=Reservation.objects.get(id=prenotazione_id)
      oggetto_prenotato_id=prenotazione_da_eliminare.IdActivityObject
      cliente_id=prenotazione_da_eliminare.IdClient
      
      #seleziona l'oggetto da liberare
      oggetto=ActivityObject.objects.get(id=oggetto_prenotato_id)
      oggetto.stato="libera"
      oggetto.save()

      #seleziona il cliente 
      cliente=Clients.objects.get(id=cliente_id)
      cliente.stato="attualmente non cliente"
      cliente.save()

      return render(request, "visualizza_per_attivita.html", context)

    elif funzione=="modifica":
        prenotazione_da_modificare=Reservation.objects.get(id=prenotazione_id)

        if request.POST:
         if request.POST['data_arrivo']!="":
            prenotazione_da_modificare.frOm_data=request.POST['data_arrivo']
         if request.POST['data_partenza']!="":
            prenotazione_da_modificare.to=request.POST['data_partenza']
         prenotazione_da_modificare.save()

         return render(request, "visualizza_per_attivita.html", context)
       
    template=loader.get_template('gestione_prenotazioni.html')
    return HttpResponse(template.render(context,request))