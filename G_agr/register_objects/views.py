from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import User,AccountManagers,FarmHouses,Activity
from .models import Earnings

# Create your views here.

def gestione_entrate(request,username,agriturismo,attivita,tipo_oggetto,funzione,filtro):
    context={}
    context['username']==username
    context['agriturismo']==agriturismo
    context['attivita']==attivita
    context['tipo_oggetto']==tipo_oggetto

    user=User.objects.get(username=username)
    user_id=user.id
    account=AccountManagers.objects.get(gestore_id=user_id)
    account_id=account.id
    agriturismo_r=FarmHouses.objects.get(IdAccountManagers_id=account_id, FarmHouseName=agriturismo)
    agriturismo_id=agriturismo_r.id
    attivita_r=Activity.objects.get(IdFarmHouses=agriturismo_id, ActivityName=attivita)
    attivita_id=attivita_r.id

    if funzione=="aggiungi":
        if request.POST:
            nuova_entrata=Earnings(
                IdAccountManagers_id=account_id,
                IdFarmHouses_id=agriturismo_id,
                IdActivity=attivita_id,
                Date=request.POST['date'],
                Quantity=request.POST['quantity']
            )
            nuova_entrata.save()
    elif funzione=="modifica":
        entrata_da_modificare=Earnings.objects.get(id=filtro)
        if request.POST:
            if request.POST['date']!="":
                nuova_data=request.post['date']
                entrata_da_modificare.Date=nuova_data
            if request.POST['quantity']!="":
                nuova_quantita=request.post['quantity']
                entrata_da_modificare.Quantity=nuova_quantita
            entrata_da_modificare.save()
    elif funzione=="elimina":
        entrata_da_eliminare=Earnings.objects.get(id=filtro)
        entrata_da_eliminare.delete()