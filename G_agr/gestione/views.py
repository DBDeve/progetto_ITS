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
from .models import Room,Clients,services,promotions,employee


# Create your views here.

@login_required(login_url='login')
def visualizza(request,argomento,scelta,username):
   context={}
   #farne una per ogni argomento (camere,servizzi, ecc...)
   context['scelta']=scelta
   context['nome_pagina']=argomento
   context['username']=username

   classi=[Clients,Room,employee,services,promotions] 

   for classe in classi:
      if scelta=="tutte":
         #valori_camere/servizzi/dipendenti/servizzi/promozioni in base all'argomento passato e lo mette in context
         context[f'valori_{classe.__name__}']=classe.objects.all().values()
      elif scelta=="occupate": 
         context[f'valori_{classe.__name__}']=classe.objects.all().values()
         context[f'{classe.__name__}_{scelta}']=classe.objects.filter(stato=scelta)
      elif scelta=="libere": 
         context[f'valori_{classe.__name__}']=classe.objects.all().values()
         context[f'{classe.__name__}_{scelta}']=classe.objects.filter(stato=scelta)

   template=loader.get_template('visualizza.html')
   return HttpResponse(template.render(context,request))



#la funzione aggiungi deve ricedere i dati dal form della pagina html quindi il 
@login_required(login_url='login')
def aggiungi(request,argomento,username):
   context={}
   context['argomento']=argomento
   context['username']=username

   if request.POST:
      #crea un nuovo oggetto Rooms
      if argomento=="camere": 
         nuova_camera=Room(
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
         nuovo_lavoratore=employee(
            name=request.POST['name'],
            codice_fiscale=request.POST['codice_fiscale'],
            iban=request.POST['iban'],
            mail=request.POST['mail'],
         )
         nuovo_lavoratore.save()
      # crea nuovo oggetto services
      elif argomento=="servizzi":
         nuovo_servizio=services(
            name=request.POST['name'],
            prize=request.POST['prize']
         )
         nuovo_servizio.save()
      # crea nuovo oggetto promotions
      elif argomento=="promozioni":
         nuova_promozione=promotions(
            name=request.POST['name']
         )
      
   template=loader.get_template('form_aggiungi.html')
   return HttpResponse(template.render(context,request))      




@login_required(login_url='login')
def modifica(request,argomento,username):
   context={}

   context ['argomento']=argomento
   context['username']=username


   if request.POST:
     
     #selezione della camera da modificare.
     number=request.POST['number']
     camera_da_modificare=Room.objects.get(number=number)

     #selezione dei dati da modificare
     nuovo_numero=request.POST['number']
     nuovo_prezzo=request.POST['prize']
     #nuova_capienza=request.POST['']

     
     camera_da_modificare.prize=nuovo_prezzo
     camera_da_modificare.save()

   template=loader.get_template('form_modifica.html')
   return HttpResponse(template.render(context,request))
   

@login_required(login_url='login')
def elimina(request,argomento,username):
   #fare in modo che possa funzionare con qualsiasi oggetto
   #definire il comportamento nel caso venga inserita una camera che non esiste
   #definire comportamento nel caso non venga inserito niente
   context={}
   context ['argomento']=argomento
   context['username']=username

   
   if request.POST:
     number=request.POST['number']
     camera_da_rimuovere=Room.objects.get(number=number)
     camera_da_rimuovere.delete()

   
   template=loader.get_template('form_elimina.html')
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

