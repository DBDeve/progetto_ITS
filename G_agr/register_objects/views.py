from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import User,AccountManagers,FarmHouses,Activity
from .models import Earnings,Expense,Clients,Employee,Salary

# Create your views here.


@login_required(login_url='login')
def gestione_entrate(request,account_id,agriturismo_id,attivita_id,funzione,filtro):
    
    context={}    
    
    #
    account=AccountManagers.objects.get(id=account_id)
    context['account_id']=account.id

    # seleziona l'agriturismo con l'id passato tramite url
    agriturismo=FarmHouses.objects.get(id=agriturismo_id)
    context['agriturismo_id']=agriturismo.id
    
    # seleziona l'attività con l'id passato tramite url
    attivita=Activity.objects.get(id=attivita_id)
    context['attivita_id']=attivita.id

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


@login_required(login_url='login')
def gestione_uscite(request,account_id,agriturismo_id,attivita_id,tipo_oggetto_id,funzione,filtro):
    
    #
    context={}

    #
    account=AccountManagers.objects.get(id=account_id)
    context['account_id']=account.id

    # seleziona l'agriturismo con l'id passato tramite url
    agriturismo=FarmHouses.objects.get(id=agriturismo_id)
    context['agriturismo_id']=agriturismo.id
    
    # seleziona l'attività con l'id passato tramite url
    attivita=Activity.objects.get(id=attivita_id)
    context['attivita_id']=attivita.id


    if funzione=="aggiungi":
        if request.POST:
            nuova_uscita=Expense(
                IdAccountManagers_id=account_id,
                IdFarmHouses_id=agriturismo_id,
                IdActivity=attivita_id,
                Date=request.POST['date'],
                Quantity=request.POST['quantity']
            )
            nuova_uscita.save()
    elif funzione=="modifica":
        uscita_da_modificare=Expense.objects.get(id=filtro)
        if request.POST:
            if request.POST['date']!="":
                nuova_data=request.post['date']
                uscita_da_modificare.Date=nuova_data
            if request.POST['quantity']!="":
                nuova_quantita=request.post['quantity']
                uscita_da_modificare.Quantity=nuova_quantita
            uscita_da_modificare.save()
    elif funzione=="elimina":
        entrata_da_eliminare=Expense.objects.get(id=filtro)
        entrata_da_eliminare.delete()


@login_required(login_url='login')
def gestione_clienti(request,account_id,agriturismo_id,attivita_id,funzione,filtro):
    context={}

    account=AccountManagers.objects.get(id=account_id)
    context['account_id']=account.id

    # seleziona l'agriturismo con l'id passato tramite url
    agriturismo=FarmHouses.objects.get(id=agriturismo_id)
    context['agriturismo_id']=agriturismo.id
    
    # seleziona l'attività con l'id passato tramite url
    attivita=Activity.objects.get(id=attivita_id)
    context['attivita_id']=attivita.id

    if funzione=="aggiungi":
        if request.POST:
            nuovo_cliente=Clients(
                IdAccountManagers_id=account_id,
                IdFarmHouses_id=agriturismo_id,
                IdActivity_id=attivita_id,
                name=request.POST['name'],
                mail=request.POST['mail'],
                number_cell=request.POST['number_cell']
            )
            nuovo_cliente.save()
    elif funzione=="modifica":
        cliente_da_modificare=Clients.objects.get(id=filtro)
        if request.POST:
            if request.POST['name']!="":
                nuovo_nome=request.post['date']
                cliente_da_modificare.name=nuovo_nome
            if request.POST['mail']!="":
                nuova_mail=request.post['quantity']
                cliente_da_modificare.mail=nuova_mail
            if request.POST['number_cell']!="":
                nuovo_numero=request.post['number_cell']
                cliente_da_modificare.number_cell=nuovo_numero
            cliente_da_modificare.save()
    elif funzione=="elimina":
        cliente_da_eliminare=Clients.objects.get(id=filtro)
        cliente_da_eliminare.delete()


@login_required(login_url='login')
def gestione_lavoratori(request,account_id,agriturismo_id,attivita_id,funzione,filtro):
    context={}
    
    #
    account=AccountManagers.objects.get(id=account_id)
    context['account_id']=account.id

    # seleziona l'agriturismo con l'id passato tramite url
    agriturismo=FarmHouses.objects.get(id=agriturismo_id)
    context['agriturismo_id']=agriturismo.id
    
    # seleziona l'attività con l'id passato tramite url
    attivita=Activity.objects.get(id=attivita_id)
    context['attivita_id']=attivita.id

    if funzione=="aggiungi":
        if request.POST:
            nuovo_lavoratore=Employee(
                IdAccountManagers_id=account_id,
                IdFarmHouses_id=agriturismo_id,
                IdActivity_id=attivita_id,
                name=request.POST['name'],
                mail=request.POST['mail'],
                number_cell=request.POST['number_cell']
            )
            nuovo_lavoratore.save()
            nuovo_stipendio=Salary(
                SalaryEmployee_id=nuovo_lavoratore.id,
                stato=request.POST['stato_salario'],
                quantity=request.POST['salary_quantity']
            )
            nuovo_stipendio.save()
    elif funzione=="modifica":
        lavoratore_da_modificare=Employee.objects.get(id=filtro)
        stipendio_da_modificare=Salary.objects.get(SalaryEmployee=lavoratore_da_modificare.id)
        if request.POST:
            if request.POST['name']!="":
                nuovo_nome=request.post['date']
                lavoratore_da_modificare.name=nuovo_nome
            if request.POST['mail']!="":
                nuova_mail=request.post['quantity']
                lavoratore_da_modificare.mail=nuova_mail
            if request.POST['number_cell']!="":
                nuovo_numero=request.post['number_cell']
                lavoratore_da_modificare.number_cell=nuovo_numero
            lavoratore_da_modificare.save()
            #inserire modifica stipendio
    elif funzione=="elimina":
        lavoratore_da_eliminare=Employee.objects.get(id=filtro)
        lavoratore_da_eliminare.delete()