from django.shortcuts import HttpResponse

from django.template import loader

#serve alla creazione dei profili
from django.contrib.auth.models import User
#serve per autenticare gli utenti
from django.contrib.auth import authenticate,login

#importa il modello question
from .models import Room,Clients,services,promotions,employee


# Create your views here.


def visualizza(request,argomento,scelta):
   context={}
   #farne una per ogni argomento (camere,servizzi, ecc...)
   context['scelta']=scelta
   context['nome_pagina']=argomento

   if argomento=="camere":
      classi=[Clients,Room] 
   elif argomento=="clienti":
      classi=[Clients]
   elif argomento=="dipendenti":
      classi=[employee]
   elif argomento=="servizzi":
      classi=[services]
   elif argomento=="promozioni":
      classi=[promotions]

   for classe in classi:
      if scelta=="tutte":
         #valori_camere/servizzi/dipendenti/servizzi/promozioni in base all'argomento passato e lo mette in context
         context[f'valori_{classe.__name__}']=classe.objects.all().values()
      else: 
         context[f'valori_{classe.__name__}']=classe.objects.all().values()
         if classe==Room:
            context[f'{classe.__name__}_{scelta}']=classe.objects.filter(stato=scelta)
   
   #print(context['Room_libera'])

   
   
   
   
   
   

   #if scelta!="tutte":
   #context[f'{argomento}_{scelta}']=classe.objects.filter(stato=scelta)


   #camere_libere = classe.objects.filter(stato="libera")
   #camere_occupate = classe.objects.filter(stato="occupata")
   #camere_prenotate = classe.objects.filter(stato="prenotata")
   #camere_chiavi = [c.name for c in Room._meta.get_fields() if c.name not in ['id','da','to','appunti_cliente','client']]
   
   

   #prende il valore client dalle camere occupate ossia l'id che camere e clienti anno in comune 
   #clienti=Clients.objects.all().values()

   #id_clienti_camera = Clients.objects.filter(id=id_camere_occupate).values("to")
   
   #context={
      #'valore_camere': camere_valore,
      #'indici_camere': camere_chiavi,
      #'nome_pagina':nome_pagina,
      #'camere_libere':camere_libere,
      #'camere_occupate':camere_occupate,
      #'scelta':scelta,
      #'clienti':clienti,
   #}

   template=loader.get_template('visualizza.html')
   return HttpResponse(template.render(context=context))

#la funzione aggiungi deve ricedere i dati dal form della pagina html quindi il 
def aggiungi(request,argomento):
   context={}
   context['argomento']=argomento

   if request.POST:
      number=request.POST['number']
      prize=request.POST['prize']
      clienti_ospitabili=request.POST['clienti_ospitabili']
      appunto_gestore=request.POST['appunti_gestore']
      appunti_cliente=request.POST['appunti_cliente']

      nuova_camera=Room(
         number=number,
         prize=prize,
         clienti_ospitabili=clienti_ospitabili,
         appunto_gestore=appunto_gestore,
         appunti_cliente=appunti_cliente
         )
      
      print(nuova_camera)
      
      nuova_camera.save()

      
   template=loader.get_template('form_aggiungi.html')
   return HttpResponse(template.render(context,request))      



def modifica(request,argomento):
   context={}

   context ['argomento']=argomento

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
   


def elimina(request,argomento):
   #fare in modo che possa funzionare con qualsiasi oggetto
   #definire il comportamento nel caso venga inserita una camera che non esiste
   #definire comportamento nel caso non venga inserito niente
   context={}
   context ['argomento']=argomento
   
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

def accedi(request):
   context={}
   if request.POST:
      username = request.POST["username"],
      password = request.POST["password"],
      user = authenticate(request, username=username, password=password)
      #if user is not None:
         #login(request, user)
         # Redirect to a success page.
         
      #else:
   
   template=loader.get_template('form_accedi.html')
   return HttpResponse(template.render(context,request))
