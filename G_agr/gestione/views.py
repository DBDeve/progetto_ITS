from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


from django.template import loader

#serve alla creazione dei profili
from django.contrib.auth.models import User
#serve per autenticare gli utenti
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

#importa il modello question
from .models import Services,Employee,AccountManagers,Earnings,FarmHouses,Expense,Salary,Clients,Promotions,Reservation


# Create your views here.

@login_required(login_url='login')
def visualizza(request,username,agriturismo,oggetto,filtro):
   context={}
   #farne una per ogni argomento (camere,servizzi, ecc...)
   context['username']=username
   context['agriturismo']=agriturismo
   context['oggetto']=oggetto
   context['filtro']=filtro

   #filtra gli utenti per l'username che gli passo (solo 1)
   user=User.objects.get(username=username)
   user_id=user.id
   #filtra gli account per l'id dell'user precentemente selezionato (solo 1)
   accounts=AccountManagers.objects.get(gestore_id=user_id)
   accounts_id=accounts.id
   # crea la lista degli agriturismi legati all'account
   context[f'valori_FarmHouses']=FarmHouses.objects.filter(IdAccountManagers_id=accounts_id)

   if user_id==accounts.gestore_id:
      # visualizza entrate
      if oggetto=="entrate":
         if agriturismo=="tutti":
            context['entrate']=Earnings.objects.filter(IdAccountManagers=accounts_id)  
         #visualizza i clienti di un singolo agriturismo
         else:
            agriturismo=FarmHouses.objects.get(IdAccountManagers_id=accounts_id, FarmHouseName=agriturismo)
            agriturismo_id=agriturismo.id
            if filtro=="tutte":
               context['entrate']=Earnings.objects.filter(IdFarmHouses=agriturismo_id)
         template=loader.get_template('visualizza/visualizza_entrate.html')
         return HttpResponse(template.render(context,request))
      
      #visualizza uscite
      elif oggetto=="uscite":
         if agriturismo=="tutti":
            context['uscite']=Expense.objects.filter(IdAccountManagers=accounts_id)  
         #visualizza i clienti di un singolo agriturismo
         else:
            agriturismo=FarmHouses.objects.get(IdAccountManagers_id=accounts_id, FarmHouseName=agriturismo)
            agriturismo_id=agriturismo.id
            if filtro=="tutte":
               context['uscite']=Expense.objects.filter(IdFarmHouses=agriturismo_id)
         template=loader.get_template('visualizza/visualizza_uscite.html')
         return HttpResponse(template.render(context,request))
      
      #visualizza lavoratori
      elif oggetto=="dipendenti":
         if agriturismo=="tutti":
            context['dipendenti']=Employee.objects.filter(IdAccountManagers=accounts_id)  
         #visualizza i clienti di un singolo agriturismo
         else:
            agriturismo=FarmHouses.objects.get(IdAccountManagers_id=accounts_id, FarmHouseName=agriturismo)
            agriturismo_id=agriturismo.id
            if filtro=="tutte":
               context['dipendenti']=Employee.objects.filter(IdFarmHouses=agriturismo_id)
         template=loader.get_template('visualizza/visualizza_dipendenti.html')
         return HttpResponse(template.render(context,request))


#la funzione aggiungi crea nuovo oggetti in base all'argomento e l'username che gli viene passato
@login_required(login_url='login')
def aggiungi(request,username,agriturismo,oggetto):
   context={}
   context['oggetto']=oggetto
   context['username']=username
   context['agriturismo']=agriturismo

   user=User.objects.get(username=username)
   user_id=user.id
   accounts=AccountManagers.objects.get(gestore_id=user_id)
   accounts_id=accounts.id
   agriturismo_s=FarmHouses.objects.get(IdAccountManagers_id=accounts_id)
   agriturismo_id=agriturismo_s.id

   if request.POST:
      #crea un nuovo oggetto Rooms (funziona)
      
      if oggetto=="promozioni":
         nuova_promozione=Promotions(
            name=request.POST['name'],
            IdFarmHouses_id=agriturismo_id
         )
         nuova_promozione.save()
         url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
         return redirect(url) 
      if oggetto=="servizzi":
         nuovo_servizio=Services(
            name=request.POST['name'],
            prize=request.POST['prize'],
            IdFarmHouses_id=agriturismo_id
         )
         nuovo_servizio.save()
         url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
         return redirect(url) 
      #crea nuovo aggetto Clients
      if oggetto=="clienti":
         nuovo_cliente=Clients(
            name=request.POST['name'],
            mail=request.POST['mail'],
            number_cell=request.POST['number_cell'],
            IdAccountManagers_id=accounts_id,
            IdFarmHouses_id=agriturismo_id
            )
         nuovo_cliente.save()
         url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
         return redirect(url) 
      # crea nuovo oggetto employee (funziona)
      if oggetto=="dipendenti":
         nuovo_lavoratore=Employee(
            name=request.POST['name'],
            codice_fiscale=request.POST['codice_fiscale'],
            iban=request.POST['iban'],
            mail=request.POST['mail'],
            IdAccountManagers_id=accounts_id,
            IdFarmHouses_id=agriturismo_id
         )
         nuovo_lavoratore.save()
         url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
         return redirect(url) 
      
      if oggetto=="uscite":
         nuova_uscita=Expense(
            Date=request.POST['date'],
            Quantity=request.POST['quantity'],
            IdAccountManagers_id=accounts_id,
            IdFarmHouses_id=agriturismo_id
         )
         nuova_uscita.save()
         url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
         return redirect(url) 
      
      if oggetto=="entrate":
         nuova_entrata=Earnings(
            Date=request.POST['date'],
            Quantity=request.POST['quantity'],
            IdAccountManagers_id=accounts_id,
            IdFarmHouses_id=agriturismo_id

         )
         nuova_entrata.save()
         url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
         return redirect(url) 
      if oggetto=="agriturismo":
         nuovo_agriturismo=FarmHouses(
            FarmHouseName=request.POST['name'],
            address=request.POST['address'],
            IdAccountManagers_id=accounts_id
            )
         nuovo_agriturismo.save() 
         url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
         return redirect(url) 

   template=loader.get_template('form/form_aggiungi.html')
   return HttpResponse(template.render(context,request))    




@login_required(login_url='login')
def modifica(request,username,agriturismo,oggetto,id_oggetto):
   context={}
   context['username']=username
   context['agriturismo']=agriturismo
   context['oggetto']=oggetto
   context['id_oggetto']=id_oggetto
   
   
   
   if oggetto=="clienti":
      cliente_da_modificare=Clients.objects.get(id=id_oggetto)
      context['oggetto_selezionato']=cliente_da_modificare
      if request.POST:
         if request.POST['mail']!="":
            nuova_mail=request.POST['mail']
            cliente_da_modificare.mail=nuova_mail
         if request.POST['number_cell']!="":
            nuovo_numero=request.POST['number_cell']
            cliente_da_modificare.number_cell=nuovo_numero
         cliente_da_modificare.save()
         url=f"/gestione/visualizza/{username}/{agriturismo}/{oggetto}/tutte"
         return redirect(url)
   if oggetto=="dipendenti":
      dipendente_da_modificare=Employee.objects.get(id=id_oggetto)
      context['oggetto_selezionato']=dipendente_da_modificare
      if request.POST:
         if request.POST['name']!="":
            nuovo_nome=request.POST['name']
            dipendente_da_modificare.name=nuovo_nome
         if request.POST['codice_fiscale']!="":
            nuovo_codice=request.POST['codice_fiscale']
            dipendente_da_modificare.codice_fiscale=nuovo_codice
         if request.POST['iban']!="":
            nuovo_iban=request.POST['iban']
            dipendente_da_modificare.iban=nuovo_iban
         
         url=f"/gestione/visualizza/{username}/{agriturismo}/{oggetto}/tutte"
         return redirect(url)

      
   
   #finché non viene inserito alcun dato la magina rimane su form_modifica.html
   template=loader.get_template('form/form_modifica.html')
   return HttpResponse(template.render(context,request))
   

@login_required(login_url='login')
def elimina(request,username,agriturismo,oggetto,id_oggetto):
   
   context={}
   context['username']=username
   context['agriturismo']=agriturismo
   context['oggetto']=oggetto
   context['id_oggetto']=id_oggetto

   # l'oggetto viene cercarto per il suo stesso id e poi eliminato. l'id viene passato attraverso la variabile "valore"
   if oggetto=="agriturismi":
      camera_da_rimuovere=FarmHouses.objects.get(id=id_oggetto)
      camera_da_rimuovere.delete()
   elif oggetto=="clienti":
      cliente_da_rimuovere=Clients.objects.get(id=id_oggetto)
      cliente_da_rimuovere.delete()
   elif oggetto=="dipendenti":
      lavoratore_da_rimuovere=Employee.objects.get(id=id_oggetto)
      lavoratore_da_rimuovere.delete()
   elif oggetto=="servizzi":
      servizio_da_rimuovere=Services.objects.get(id=id_oggetto)
      servizio_da_rimuovere.delete()
   elif oggetto=="promozioni":
      promozione_da_rimuovere=Promotions.objects.get(id=id_oggetto)
      promozione_da_rimuovere.delete()
   elif oggetto=="entrate":
      entrata_da_rimuovere=Earnings.objects.get(id=id_oggetto)
      entrata_da_rimuovere.delete()
   elif oggetto=="uscite":
      uscite_da_rimuovere=Expense.objects.get(id=id_oggetto)
      uscite_da_rimuovere.delete()

   
   url=f"/gestione/{username}/{agriturismo}/{oggetto}/visualizza/tutte"
   return redirect(url)








   template=loader.get_template('gestione_clienti_presenti.html')
   return HttpResponse(template.render(context,request))



#crea verifica se l'accounta ha un agriturismo e se non ce l'ha lo fa aggiungere
@login_required(login_url='login')
def gestione_agtriturismi(request,username,funzione,filtro):

   context={}
   context['username']=username

   user=User.objects.get(username=username)
   user_id=user.id
   account=AccountManagers.objects.get(gestore_id=user_id)
   account_id=account.id

   agriturismi=FarmHouses.objects.filter(IdAccountManagers_id=account_id)
   context['agriturismi']=agriturismi
   if funzione=="verifica_aggiungi":
      if agriturismi.exists():
         context['frase']="scegli agriturismo"
         context['esiste']="True"
         context['agriturismi']=agriturismi

         return render(request, "gestione_agriturismi.html", context)
      else:
         context['esiste']="False"
         context['frase']="crea agriturismo"
         if request.POST:
            nuovo_agriturismo=FarmHouses(
               FarmHouseName=request.POST['name'],
               address=request.POST['address'],
               IdAccountManagers_id=account_id
            )
            nuovo_agriturismo.save() 
         return render(request, "gestione_agriturismi.html", context)
   elif funzione=="aggiungi":
      context['funzione']=funzione
      if request.POST:
         nuovo_agriturismo=FarmHouses(
            FarmHouseName=request.POST['name'],
            address=request.POST['address'],
            IdAccountManagers_id=account_id
         )
         nuovo_agriturismo.save() 
         url=f"/gestione/{username}/agriturismo/verifica_aggiungi/nessuno"
         return redirect(url)
      #finché non c'è una richiesta rimane sulla pagina gestione_agriturismi.html
      return render(request, "gestione_agriturismi.html", context)
   elif funzione=="elimina":
      context['funzione']=funzione
      camera_da_rimuovere=FarmHouses.objects.get(id=filtro)
      camera_da_rimuovere.delete()
      url=f"/gestione/{username}/agriturismo/verifica_aggiungi/nessuno"
      return redirect(url)



def cambia_password(request):
   context={}

   if request.POST:
      user=User.objects.get(username=request.POST['username'])
      nuova_password=request.POST['nuova_password']
      username = request.POST.get('username')
      try:
         user = User.objects.get(username=username)
         # Imposta la nuova password con hashing
         user.set_password(nuova_password)
         user.save()
         messages.success(request, 'Password aggiornata con successo.')
         return redirect('login')
      except User.DoesNotExist:
         messages.error(request, 'Utente non trovato.')
         return redirect('cambia_password')
   
   template=loader.get_template('form/form_cambia_password.html')
   return HttpResponse(template.render(context,request))
   


#fa registrare un nuovo utente
def registrati(request):
   context={}

   if request.POST:
      #crea un nuovo user
      user = User.objects.create_user(
         username=request.POST['username'],
         email=request.POST['email'],
         password=request.POST['password'],
         first_name=request.POST['first_name'],
         last_name=request.POST['last_name'],
         )
      user.save()
      
      #crea un nuovo account collegato allo user appena creato
      IdUser=user.id
      nuovo_account=AccountManagers(
         gestore_id=IdUser
      )
      nuovo_account.save()

      #rendirizza alla pagina di login
      url=f"login"
      return render(request, "form/form_accedi.html", {"argomento":'log in | accedi'})


   template=loader.get_template('form/form_registrati.html')
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
         url=f"{user.username}/agriturismo/verifica_aggiungi/nessuno"
         return redirect(url)
      else:
         messages.error(request, f"si è verificato un problema. riprova")
         #return redirect('http://127.0.0.1:8000/gestione/visualizza/camere/tutte')
         return render(request, "form/form_accedi.html", {"argomento":'log in | accedi'})
   else:
      return render(request, "form/form_accedi.html", {"argomento":'log in | accedi'})



#fa fare il logout e rendirizza alla pagina di login
def log_out(request):
   logout(request)
   return redirect('login')

   