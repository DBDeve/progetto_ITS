from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import User,AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject

# Create your views here.


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



@login_required(login_url='login')
def gestione_attivita(request,username,agriturismo,funzione,filtro):
   context={}
   context['username']=username
   context['agriturismo']=agriturismo
   context['funzione']=funzione
   context['filtro']=filtro

   user=User.objects.get(username=username)
   user_id=user.id
   account=AccountManagers.objects.get(gestore_id=user_id)
   account_id=account.id
   agriturismo=FarmHouses.objects.get(IdAccountManagers_id=account_id, FarmHouseName=agriturismo)
   agriturismo_id=agriturismo.id
   attivita=Activity.objects.filter(IdFarmHouses=agriturismo_id)

   if funzione=="verifica_scegli":
      if attivita.exists():
         context['frase']="scegli attivita"
         context['esiste']="True"
         context['attivita']=attivita
         return render(request, "gestione_attivita.html", context)
      else:
         context['esiste']="False"
         context['frase']="crea agriturismo"
         if request.POST:
            nuova_attivita=Activity(
               ActivityName=request.POST['activity_name'],
               ActivityType=request.POST['activity_type'],
               IdFarmHouses=agriturismo_id
            )
            nuova_attivita.save() 
         
         return render(request, "gestione_attivita.html", context)
   elif funzione=="aggiungi":
      nuova_attivita=Activity(
         ActivityName=request.POST['activity_name'],
         ActivityType=request.POST['activity_type'],
         IdFarmHouses=agriturismo_id
      )
      nuova_attivita.save() 
   elif funzione=="elimina":
      attivita_da_rimuovere=Activity.objects.get(id=filtro)
      attivita_da_rimuovere.delete()
   elif funzione=="aggiungi_camere":
      attivita_camere=Activity(
         ActivityType="camere",
         ActivityName="camere",
         IdFarmHouses_id=agriturismo_id
      )
      attivita_camere.save()
      gruppo_oggetti=TypeObjects(
         IdGroupObjects_id=attivita_camere.Id,
         GroupName="camera"
      )
      gruppo_oggetti.save()
   elif funzione=="aggiungi_ristorante":
      attivita_ristorante=Activity(
         ActivityType="ristorante",
         ActivityName=request.POST['name'],
         IdFarmHouses_id=agriturismo_id
      )
      attivita_ristorante.save()
      gruppo_oggetti_tavoli=TypeObjects(
         IdGroupObjects_id=attivita_ristorante.Id,
         GroupName="tavoli"
      )
      gruppo_oggetti_tavoli.save()
      gruppo_oggetti_menu=TypeObjects(
         IdGroupObjects_id=attivita_ristorante.Id,
         GroupName="piatti del menù"
      )
      gruppo_oggetti_menu.save()

   
   return render(request, "gestione_attivita.html", context)



@login_required(login_url='login')
def gestione_tipo_oggetto(request,username,agriturismo,attivita,funzione,filtro):
   context={}
   context['username']=username
   context['agriturismo']=agriturismo
   context['attivita']=attivita
   context['funzione']=funzione
   context['filtro']=filtro

   user=User.objects.get(username=username)
   user_id=user.id
   account=AccountManagers.objects.get(gestore_id=user_id)
   account_id=account.id
   agriturismo=FarmHouses.objects.get(IdAccountManagers_id=account_id, FarmHouseName=agriturismo)
   agriturismo_id=agriturismo.id
   attivita=Activity.objects.get(IdFarmHouses=agriturismo_id, ActivityName=attivita)
   attivita_id=attivita.id
   
   if funzione=="aggiungi":
      if request.POST:
         nuovo_tipo_oggetto=TypeObjects(
            IdActivity=attivita_id,
            TypeName=request.POST['type_name']
         )
         nuovo_tipo_oggetto.save()
   elif funzione=="modifica":
      tipo_oggetto_da_modificare=TypeObjects.objects.get(id=filtro)
      if request.POST:
         if request.POST['new_type']!="":
            tipo_oggetto_da_modificare.TypeName=request.POST['new_type']
      tipo_oggetto_da_modificare.save()
   elif funzione=="elimina":
      tipo_oggetto_da_eliminare=TypeObjects.objects.get(Id=filtro)
      tipo_oggetto_da_eliminare.delete()
   return render(request, "gestione_tipo_oggetti.html", context)


@login_required(login_url='login')
def gestione_oggetto_singolo(request,username,agriturismo,attivita,tipo_oggetto,funzione,filtro):
   context={}
   context['username']=username
   context['agriturismo']=agriturismo
   context['attivita']=attivita
   context['tipo_oggetto']=tipo_oggetto
   context['funzione']=funzione
   context['filtro']=filtro

   user=User.objects.get(username=username)
   user_id=user.id
   account=AccountManagers.objects.get(gestore_id=user_id)
   account_id=account.id
   agriturismo=FarmHouses.objects.get(IdAccountManagers_id=account_id, FarmHouseName=agriturismo)
   agriturismo_id=agriturismo.id
   attivita=Activity.objects.get(IdFarmHouses=agriturismo_id, ActivityName=attivita)
   attivita_id=attivita.id
   tipo_oggetto_s=TypeObjects.objects.get(IdActivity=attivita_id, TypeName=tipo_oggetto)
   tipo_oggetto_id=tipo_oggetto_s.id

   
   if funzione=="aggiungi":
      if request.POST:
            nuovo_oggetto=ActivityObject(
               IdTypeObjects=tipo_oggetto_id,
               ObjectNumber=request.POST['numero_oggetto'],
               ObjectPrize=request.POST['prezzo_oggetto'],
               stato="non disponibile"
            )
            nuovo_oggetto.save()
      return render(request, "gestione_oggetto_singolo.html", context)
   elif funzione=="modifica":
      oggetto_da_modificare=ActivityObject.objects.get(id=filtro)
      if request.POST:
         if request.POST['new_number']!="":
            oggetto_da_modificare.ObjectNumber=request.POST['new_number']
         if request.POST['ner_prize']!="":
            oggetto_da_modificare.ObjectPrize=request.POST['new_Prize']
         if request.POST['stato']!="":
            oggetto_da_modificare.stato=request.POST['stato']
   elif funzione=="elimina":
      oggetto_da_eliminare=ActivityObject.objects.get(id=filtro)
      oggetto_da_eliminare.delete()
   return render(request, "gestione_oggetto_singolo.html", context)