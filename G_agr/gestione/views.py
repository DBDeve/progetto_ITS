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
def visualizza(request,argomento,scelta,username):
   context={}
   #farne una per ogni argomento (camere,servizzi, ecc...)
   context['scelta']=scelta
   context['nome_pagina']=argomento
   context['username']=username

   classi=[Clients,Rooms,Employee,Expense,Earnings,FarmHouses]  
   #utenti
   users=User.objects.all().values()
   #use=User.objects.get('id')
   #profili
   #accounts=AccountManagers.objects.all().values()
   

   #itera tutti gli utenti
   for user in users:
      #verifica se l'username passato dalla funzione corrisponde a quello dell'user
      if user['username']==username:
         #crea un variabile con l'id dell'user
         user_id=user['id']
         #crea una lista con i valori id di gestore dalla tabella AccountManager
         accounts_id=AccountManagers.objects.all().values_list('gestore_id', flat=True)
         
         if user_id in accounts_id:
            #accounts_id=user_id
            if scelta=="tutte":
                  for classe in classi:
                  #valori_camere/servizzi/dipendenti/servizzi/promozioni in base al valore della variabile scelta passato e lo mette in context
                     context[f'valori_{classe.__name__}']=classe.objects.all().values()
            else:
               if scelta=="occupata": 
                     context[f'valori_Room']=Rooms.objects.all().values()
                     context[f'valori_Clients']=Clients.objects.all().values()
                     context[f'Room_{scelta}']=Rooms.objects.filter(stato=scelta)
               elif scelta=="libera": 
                     context[f'valori_Room']=Rooms.objects.all().values()
                     context[f'Room_{scelta}']=Rooms.objects.filter(stato=scelta)

   template=loader.get_template('visualizza.html')
   return HttpResponse(template.render(context,request))



#la funzione aggiungi crea nuovo oggetti in base all'argomento e l'username che gli viene passato
@login_required(login_url='login')
def aggiungi(request,argomento,username):
   context={}
   context['argomento']=argomento
   context['username']=username


   
   if request.POST:
      #crea un nuovo oggetto Rooms
      if argomento=="camere": 
         nuova_camera=Rooms(
            number=request.POST['number'],
            prize=request.POST['prize'],
            clienti_ospitabili=request.POST['clienti_ospitabili'],
            appunto_gestore=request.POST['appunti_gestore'],
            appunti_cliente=request.POST['appunti_cliente'],
            )
         nuova_camera.save()
      #crea nuovo aggetto Clients
      elif argomento=="clienti":
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

   
   if request.POST:
      if argomento=="camere":
         number=request.POST['number']
         camera_da_rimuovere=Rooms.objects.get(number=number)
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
   users=User.objects.all().values()
   

   #itera tutti gli utenti
   for user in users:
      #verifica se l'username passato dalla funzione corrisponde a quello dell'user
      if user['username']==username:
         #crea un variabile con l'id dell'user
         user_id=user['id']
         #crea una lista con i valori id di gestore dalla tabella AccountManager
         accounts_gestore_id=AccountManagers.objects.all().values_list('gestore_id', flat=True) 

         if user_id in accounts_gestore_id and request.POST:
            #prende il l'account con un valore gestore_id uquale a quello dell'user
            accounts=AccountManagers.objects.get(gestore_id=user_id)
            if argomento=="agriturismo":
               nuovo_agriturismo=FarmHouses(
                  name=request.POST['name'],
                  address=request.POST['address'],
                  FarmHousesAccountManagers=accounts['id']         
               )
               nuovo_agriturismo.save()
            #if argomento==""
         template=loader.get_template('form_crea_agriturismo.html')
         return HttpResponse(template.render(context,request))
      
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

