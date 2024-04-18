from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.template import loader

#serve alla creazione dei profili
from django.contrib.auth.models import User
#serve per autenticare gli utenti
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

#importa il modello question
from .models import Rooms,Services,Employee,AccountManagers,Earnings,FarmHouses,Expense,Salary,Clients,Promotions


# Create your views here.

@login_required(login_url='login')
def visualizza(request,username,agriturismo,argomento,scelta):
   context={}
   #farne una per ogni argomento (camere,servizzi, ecc...)
   context['username']=username
   context['agriturismo']=agriturismo
   context['nome_pagina']=argomento
   context['scelta']=scelta
   
   classi_accounts=[Earnings,FarmHouses,Expense,Employee,Clients]
   classi_agriturismi=[Rooms,Services,Promotions,Employee,Clients] 
   context[f'valori_FarmHouses']=FarmHouses.objects.all().values()
   

   #filtra gli utenti per l'username che gli passo (solo 1)
   user=User.objects.get(username=username)
   user_id=user.id
   #filtra gli account per l'id dell'user precentemente selezionato (solo 1)
   accounts=AccountManagers.objects.get(gestore_id=user_id)
   accounts_id=accounts.id
   #filtra gli agriturismi per l'id il nome dell'agriturismo nel
   agriturismo=FarmHouses.objects.get(FarmHouseName=agriturismo)
   agriturismo_id=agriturismo.id

   if user_id==accounts.gestore_id:
      #visualizza i dati in tutti gli agriturismi
      if agriturismo=="tutti":
         if scelta=="tutte":
            for classe in classi_accounts:
               context[f'valori_{classe.__name__}']=classe.objects.filter(IdAccountManagers=accounts_id)
         elif scelta=="occupata": 
               context[f'valori_Rooms']=Rooms.objects.all().values()
               context[f'valori_Clients']=Clients.objects.all().values()
               context[f'Room_{scelta}']=Rooms.objects.filter(stato=scelta)
         elif scelta=="libera": 
               context[f'valori_Room']=Rooms.objects.all().values()
               context[f'Room_{scelta}']=Rooms.objects.filter(stato=scelta)
      #visualizza i singoli dati dei singoli agriturismi
      else:
         if scelta=="tutte":
            for classe in classi_agriturismi:
               context[f'valori_{classe.__name__}']=classe.objects.filter(IdFarmHouses=agriturismo_id)
         elif scelta=="occupata": 
               context[f'valori_Rooms']=Rooms.objects.all().values()
               context[f'valori_Clients']=Clients.objects.all().values()
               context[f'Room_{scelta}']=Rooms.objects.filter(stato=scelta)
         elif scelta=="libera": 
               context[f'valori_Room']=Rooms.objects.all().values()
               context[f'Room_{scelta}']=Rooms.objects.filter(stato=scelta)
         

   template=loader.get_template('visualizza.html')
   return HttpResponse(template.render(context,request))



#la funzione aggiungi crea nuovo oggetti in base all'argomento e l'username che gli viene passato
@login_required(login_url='login')
def aggiungi(request,username,agriturismo,argomento,):
   context={}
   context['argomento']=argomento
   context['username']=username
   context['agriturismo']=agriturismo

   user=User.objects.get(username=username)
   user_id=user.id
   accounts=AccountManagers.objects.get(gestore_id=user_id)
   accounts_id=accounts.id
   agriturismo=FarmHouses.objects.filter(IdAccountManagers=accounts_id)
   #agriturismo_id=agriturismo.id


   
   if request.POST:
      #crea un nuovo oggetto Rooms
      
      #crea nuovo aggetto Clients
      if argomento=="clienti":
         nuovo_cliente=Clients(
            name=request.POST['name'],
            mail=request.POST['mail'],
            number_cell=request.POST['number_cell']
            )
         nuovo_cliente.save()
      # crea nuovo oggetto employee
      elif argomento=="lavoratori":
         nuovo_lavoratore=Employee(
            name=request.POST['name'],
            codice_fiscale=request.POST['codice_fiscale'],
            iban=request.POST['iban'],
            mail=request.POST['mail'],
         )
         nuovo_lavoratore.save()
      elif argomento=="camere": 
         nuova_camera=Rooms(
            number=request.POST['number'],
            prize=request.POST['prize'],
            clienti_ospitabili=request.POST['clienti_ospitabili'],
            appunto_gestore=request.POST['appunti_gestore'],
            appunti_cliente=request.POST['appunti_cliente'],
            )
         nuova_camera.save()
      # crea nuovo oggetto services
      elif argomento=="servizzi":
         nuovo_servizio=Services(
            name=request.POST['name'],
            prize=request.POST['prize']
         )
         nuovo_servizio.save()
      # crea nuovo oggetto promotions
      elif argomento=="promozioni":
         nuova_promozione=Promotions(
            name=request.POST['name']
         )
      
   template=loader.get_template('form_aggiungi.html')
   return HttpResponse(template.render(context,request))      




@login_required(login_url='login')
def modifica(request,argomento,username,valore):
   context={}
   context['valore']=valore
   context ['argomento']=argomento
   context['username']=username


   if request.POST:
     if argomento=="camere":
         number=valore
         #selezione dell'oggetto da modificare 
         camera_da_modificare=Rooms.objects.get(number=number)
         #controlla se i dati inviato abbiano un valore. se ce l'hanno quel valore viene sostituito a quello dell'oggetto
         if request.POST['prize']!="":
           nuovo_prezzo=request.POST['prize']
           camera_da_modificare.prize=nuovo_prezzo
         if request.POST['number']!="":
           nuovo_numero=request.POST['number']
           camera_da_modificare.number=nuovo_numero
         if request.POST['stato']!="":
           nuovo_stato=request.POST['stato']
           camera_da_modificare.stato=nuovo_stato
         #salvataggio dell'oggetto con i dati modificati
         camera_da_modificare.save()
         #ridirezionamento alla fine della modifica
         url=f"/gestione/visualizza/{username}/camere/tutte"
         return redirect(url)
     #selezione dei dati da modificare
     
     
     #nuova_capienza=request.POST['']

     
     
     #return render(request, "visualizza.html", {username, 'camere'})
   
   #finché non viene inserito alcun dato la magina rimane su form_modifica.html
   template=loader.get_template('form_modifica.html')
   return HttpResponse(template.render(context,request))
   

@login_required(login_url='login')
def elimina(request,argomento,username):
   #definire il comportamento nel caso venga inserita una camera che non esiste
   #definire comportamento nel caso non venga inserito niente
   context={}
   context ['argomento']=argomento
   context['username']=username

   user=User.objects.get(username=username)
   user_id=user.id
   accounts=AccountManagers.objects.get(gestore_id=user_id)

   if user_id==accounts.gestore_id:
      if request.POST:
         if argomento=="agriturismi":
            FarmHouseName=request.POST['name']
            camera_da_rimuovere=FarmHouses.objects.get(FarmHouseName=FarmHouseName)
            camera_da_rimuovere.delete()
         elif argomento=="clienti":
            name=request.POST['name']
            mail=request.POST['mail']
            number_cell=request.POST['number_cell']
            cliente_da_rimuovere=Clients.objects.get(name=name, mail=mail, number_cell=number_cell)
            cliente_da_rimuovere.delete()
         elif argomento=="lavoratori":
            codice_fiscale=request.POST['codice_fiscale']
            lavoratore_da_rimuovere=Employee.objects.get(codice_fiscale=codice_fiscale)
            lavoratore_da_rimuovere.delete()
         elif argomento=="servizzi":
            name=request.POST['name']
            servizio_da_rimuovere=Services.objects.get(name=name)
            servizio_da_rimuovere.delete()
         elif argomento=="promozioni":
            name=request.POST['name']
            promozione_da_rimuovere=Promotions.objects.get(name=name)
            promozione_da_rimuovere.delete()


   
   template=loader.get_template('form_elimina.html')
   return HttpResponse(template.render(context,request))



#crea gli oggetti che vengono associati alla tabella AccountManager
@login_required(login_url='login')
def aggiungi_oggetto_account(request,argomento,username):
   context={}
   context['username']=username
   context['argomento']=argomento

   user=User.objects.get(username=username)
   user_id=user.id
   accounts=AccountManagers.objects.get(gestore_id=user_id)

   if request.POST:
      if argomento=="agriturismi":
         nuovo_agriturismo=FarmHouses(
            FarmHouseName=request.POST['name'],
            address=request.POST['address'],
            FarmHousesAccountManagers=accounts
         )
         nuovo_agriturismo.save() 
         
   template=loader.get_template('form_crea_agriturismo.html')
   return HttpResponse(template.render(context,request))








#fa registrare un nuovo utente
def registrati(request):
   context={}

   if request.POST:

      user = User.objects.create_user(
         username=request.POST['username'],
         email=request.POST['email'],
         password=request.POST['password'],
         first_name=request.POST['first_name'],
         last_name=request.POST['last_name'],
         )
      user.save()

   template=loader.get_template('form_registrati.html')
   return HttpResponse(template.render(context,request))



#fa accedere un utente già registrato
def accedi(request):
   if request.method=="POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      #verifica che l'user sia stato autenticato
      if  user is not None:
         login(request, user)
         messages.success(request, f"benvenuto {user.username}")
         url=f"visualizza/{user.username}/camere/tutte"
         return redirect(url)
      else:
         messages.error(request, f"si è verificato un problema. riprova")
         #return redirect('http://127.0.0.1:8000/gestione/visualizza/camere/tutte')
         return render(request, "form_accedi.html", {"argomento":'log in | accedi'})
   else:
      return render(request, "form_accedi.html", {"argomento":'log in | accedi'})



#fa fare il logout e permette di fare un nuovo accesso sulla stessa pagina 
def log_out(request):
   logout(request)
   if request.method=="POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      #verifica che l'user sia stato autenticato
      if  user is not None:
         login(request, user)
         messages.success(request, f"benvenuto {user.username}")
         url=f"visualizza/{user.username}/camere/tutte"
         return redirect(url)
      else:
         messages.error(request, f"si è verificato un problema. riprova")
         #return redirect('http://127.0.0.1:8000/gestione/visualizza/camere/tutte')
         return render(request, "form_accedi.html", {"argomento":'log in | accedi'})
   else:
      return render(request, "form_accedi.html", {"argomento":'log in | accedi'})

