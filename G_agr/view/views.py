from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import User,AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject
from .models import Earnings,Expense,Clients,Employee,Salary
from .models import Reservation, visit

# Create your views here.

@login_required(login_url='login')
def visualizza_per_attivita(request,username,agriturismo,attivita,filtro):
    context={}
    context['username']=username
    context['agriturismo']=agriturismo
    context['attivita']=attivita
    context['filtro']=filtro
    
    
    user=User.objects.get(username=username)
    user_id=user.id
    account=AccountManagers.objects.get(gestore_id=user_id)
    account_id=account.id
    agriturismo=FarmHouses.objects.get(IdAccountManagers_id=account_id, FarmHouseName=agriturismo)
    agriturismo_id=agriturismo.id
    attivita=Activity.objects.get(IdFarmHouses=agriturismo_id, ActivityName=attivita)
    attivita_id=attivita.id
    
    
    context['entrate_attivita']=Earnings.objects.filter(IdActivity_id=attivita_id)
    context['uscite_attivita']=Expense.objects.filter(IdActivity_id=attivita_id)
    context['clienti_attivita']=Clients.objects.filter(IdActivity_id=attivita_id)
    context['lavoratori_attivita']=Employee.objects.filter(IdActivity_id=attivita_id)
    
    
    #return render(request, "gestione_oggetto_singolo.html", context)
