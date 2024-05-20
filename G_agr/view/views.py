from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import User,AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject
from .models import Earnings,Expense,Clients,Employee,Salary
from .models import Reservation, visit

# Create your views here.

@login_required(login_url='login')
def visualizza_per_attivita(request,account_id,agriturismo_id,attivita_id,lista):
    context={}
    context['lista']=lista

    account=AccountManagers.objects.get(id=account_id)
    context['account_id']=account.id
    
    #filtra le informazioni
    agriturismo=FarmHouses.objects.get(id=agriturismo_id)
    context['agriturismo_id']=agriturismo.id
    context['agriturismo_name']=agriturismo.FarmHouseName
    
    attivita=Activity.objects.get(id=attivita_id)
    context['attivita_id']=attivita.id
    context['attivita_name']=attivita.ActivityType
    
    #crea una query con tutte le attività legate all'agriturismo
    context['lista_attivita_agriturismo']=Activity.objects.filter(IdFarmHouses=agriturismo_id)
    context['lista_gruppo_oggetti_attivita']=TypeObjects.objects.filter(IdActivity=attivita_id)

    
    #crea delle query degli oggetti legati alle attività
    if lista=="entrate":
        context['entrate_attivita']=Earnings.objects.filter(IdActivity_id=attivita_id)
        context['lista']=lista
    elif lista=="uscite":
        context['uscite_attivita']=Expense.objects.filter(IdActivity_id=attivita_id)
        context['lista']=lista
    elif lista=="clienti":
        context['clienti_attivita']=Clients.objects.filter(IdActivity_id=attivita_id)
        context['lista']=lista
    elif lista=="lavoratori":
        context['lavoratori_attivita']=Employee.objects.filter(IdActivity_id=attivita_id)
        context['lista']=lista
     
    #manda il contenuto delle query alla pagine "visualizza_per_attivita.html"
    return render(request, "visualizza_per_attivita.html", context)


@login_required(login_url='login')
def visualizza_per_gruppi_oggetti(request,account_id,agriturismo_id,attivita_id,gruppo_oggetti_id,filtro):
    context={}
    
    #filtra le informazioni
    agriturismo=FarmHouses.objects.get(id=agriturismo_id)
    context['agriturismo_id']=agriturismo.id
    attivita=Activity.objects.get(id=attivita_id)
    context['attivita_id']=attivita.id
    
    #crea una query con tutte le attività legate all'agriturismo
    context['lista_attivita_agriturismo']=Activity.objects.filter(IdFarmHouses=agriturismo_id)
    context['lista_gruppo_oggetti_attivita']=TypeObjects.objects.filter(IdActivity=attivita_id)
    context['lista_oggetti_gruppo']=ActivityObject.objects.filter(IdTypeObjects=gruppo_oggetti_id)

    
    #manda il contenuto delle query alla pagine "visualizza_per_attivita.html"
    return render(request, "visualizza_per_attivita.html", context)