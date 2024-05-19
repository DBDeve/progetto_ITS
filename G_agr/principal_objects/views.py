from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.decorators import login_required

from .models import User,AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject

# Create your views here.


#funzione per la gestione degli oggetti FarmHouses
@login_required(login_url='login')
def gestione_agtriturismi(request,account_id,funzione,filtro):
   #creo un dizionario vuoto
   context={}

   #creo una query con l'account selezionato e lo metto nel dizionario
   account=AccountManagers.objects.get(id=account_id)
   context['account_id']=account.id

   #creo una lista di tutti gli agriturismi collegati all'account selezionato
   agriturismi=FarmHouses.objects.filter(IdAccountManagers_id=account_id)


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
         url=f"/principal_objects/{account_id}/agriturismo/verifica_aggiungi/None"
         return redirect(url)
      #finché non c'è una richiesta rimane sulla pagina gestione_agriturismi.html
      return render(request, "gestione_agriturismi.html", context)
   elif funzione=="elimina":
      context['funzione']=funzione
      camera_da_rimuovere=FarmHouses.objects.get(id=filtro)
      camera_da_rimuovere.delete()
      url=f"/principal_objects/{account_id}/agriturismo/verifica_aggiungi/None"
      return redirect(url)



@login_required(login_url='login')
def gestione_attivita(request,account_id,agriturismo_id,funzione,filtro):
   context={}
   context['funzione']=funzione
   context['filtro']=filtro
   
   #crea una query con l'account selezionato attraverso l'id passato tramite url
   account=AccountManagers.objects.get(id=account_id)
   context['account_id']=account.id

   #crea una query con l'agriturismo selezionato attraverso l'id passato tramite url
   agriturismo=FarmHouses.objects.get(id=agriturismo_id)
   context['agriturismo_name']=agriturismo.FarmHouseName
   context['agriturismo_id']=agriturismo.id

   #crea una query con la lista delle attività legate all'agriturismo
   attivita=Activity.objects.filter(IdFarmHouses=agriturismo_id)

   if funzione=="verifica_scegli":
      if attivita.exists():
         context['frase']="scegli attivita"
         context['esiste']="True"
         context['attivita']=attivita
         return render(request, "gestione_attivita.html", context)
      else:
         context['esiste']="False"
         context['frase']="crea attività"
         if request.POST:
            nuova_attivita=Activity(
               ActivityName=request.POST['activity_name'],
               ActivityType=request.POST['activity_type'],
               IdFarmHouses_id=agriturismo_id
            )
            nuova_attivita.save() 
         
         return render(request, "gestione_attivita.html", context)
   elif funzione=="aggiungi":
      if request.POST:
         nuova_attivita=Activity(
            ActivityName=request.POST['activity_name'],
            ActivityType=request.POST['activity_type'],
            IdFarmHouses_id=agriturismo_id
         )
         nuova_attivita.save() 
         url=f"/principal_objects/{account_id}/{agriturismo_id}/attivita/verifica_scegli/None"
         return redirect(url)    
   elif funzione=="elimina":
      attivita_da_rimuovere=Activity.objects.get(id=filtro)
      attivita_da_rimuovere.delete()
      url=f"/principal_objects/{account_id}/{agriturismo_id}/attivita/verifica_scegli/None"
      return redirect(url)
   
   elif funzione=="aggiungi_camere":
      if request.POST:
         attivita_camere=Activity(
            ActivityType="camere",
            ActivityName=request.POST['activity_name'],
            IdFarmHouses_id=agriturismo_id
         )
         attivita_camere.save()
         gruppo_oggetti=TypeObjects(
            IdActivity=attivita_camere,
            TypeName="camera"
         )
         gruppo_oggetti.save()
         url=f"/principal_objects/{account_id}/{agriturismo_id}/attivita/verifica_scegli/None"
         return redirect(url)
   elif funzione=="aggiungi_ristorante":
      if request.POST:
         attivita_ristorante=Activity(
            ActivityType="ristorante",
            ActivityName=request.POST['activity_name'],
            IdFarmHouses_id=agriturismo_id
         )
         attivita_ristorante.save()
         gruppo_oggetti_tavoli=TypeObjects(
            IdActivity=attivita_ristorante,
            TypeName="tavolo"
         )
         gruppo_oggetti_tavoli.save()
         gruppo_oggetti_menu=TypeObjects(
            IdActivity=attivita_ristorante,
            TypeName="piatto del menù"
         )
         gruppo_oggetti_menu.save()
         url=f"/principal_objects/{account_id}/{agriturismo_id}/attivita/verifica_scegli/None"
         return redirect(url)
   elif funzione=="aggiungi_stalle":
      if request.POST:
         attivita_stalle=Activity(
            ActivityType="stalle",
            ActivityName=request.POST['activity_name'],
            IdFarmHouses_id=agriturismo_id
         )
         attivita_stalle.save()
         gruppo_oggetti_tavoli=TypeObjects(
            IdActivity=attivita_stalle,
            TypeName="stalla"
         )
         gruppo_oggetti_tavoli.save()
         url=f"/principal_objects/{account_id}/{agriturismo_id}/attivita/verifica_scegli/None"
         return redirect(url)
   elif funzione=="aggiungi_piscina":
      if request.POST:
         attivita_piscina=Activity(
            ActivityType="piscina",
            ActivityName=request.POST['activity_name'],
            IdFarmHouses_id=agriturismo_id
         )
         attivita_piscina.save()
         gruppo_oggetti_ombrelloni=TypeObjects(
            IdActivity=attivita_piscina,
            TypeName="ombrellone"
         )
         gruppo_oggetti_ombrelloni.save()
         gruppo_oggetti_sdraio=TypeObjects(
            IdActivity=attivita_piscina,
            TypeName="sdraio"
         )
         gruppo_oggetti_sdraio.save()
         url=f"/principal_objects/{account_id}/{agriturismo_id}/attivita/verifica_scegli/None"
         return redirect(url)

   return render(request, "gestione_attivita.html", context)



@login_required(login_url='login')
def gestione_tipo_oggetto(request,account_id,agriturismo_id,attivita_id,funzione,filtro):
   context={}
   
   #crea una query con l'account selezionato attraverso l'id passato tramite url
   account=AccountManagers.objects.get(id=account_id)
   context['account_id']=account.id
   
   #crea una query con l'agriturismo
   agriturismo=FarmHouses.objects.get(id=agriturismo_id)
   context['agriturismo_name']=agriturismo.FarmHouseName
   context['agriturismo_id']=agriturismo.id

   #crea una query con la lista delle attività legate all'agriturismo
   attivita=Activity.objects.get(id=attivita_id)
   context['attivita_type']=attivita.ActivityType
   context['attivita_name']=attivita.ActivityName
   context['attivita_id']=attivita.id

   #crea una lista di tutti i gruppi di oggetti legati all'attività
   tipi_oggetti=TypeObjects.objects.filter(IdActivity=attivita.id)

   #
   context['funzione']=funzione
   context['filtro']=filtro

   
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
def gestione_oggetto_singolo(request,account_id,agriturismo_id,attivita_id,tipo_oggetto_id,funzione,filtro):
   context={}

   #crea una query con l'account selezionato attraverso l'id passato tramite url
   account=AccountManagers.objects.get(id=account_id)
   context['account_id']=account.id
   
   #crea una query con l'id dell'agriturismo passata tramite url
   agriturismo=FarmHouses.objects.get(id=agriturismo_id)
   context['agriturismo_name']=agriturismo.FarmHouseName
   context['agriturismo_id']=agriturismo.id

   #crea una query con l'id dell'attivita passata tramite url
   attivita=Activity.objects.get(id=attivita_id)
   context['attivita_id']=attivita.id
   context['attivita_type']=attivita.ActivityType
   context['attivita_name']=attivita.ActivityName

   #crea una query con l'id del gruppo oggetti passata tramite url
   tipi_oggetti=TypeObjects.objects.get(id=tipo_oggetto_id)
   context['tipi_oggetti_id']=tipi_oggetti.id
   context['tipi_oggetti_name']=tipi_oggetti.TypeName

   # crea una lista di tutti gli oggetti legati ad un certo gruppo
   oggetti=ActivityObject.objects.filter(IdTypeObjects=tipo_oggetto_id)

   #
   context['funzione']=funzione
   context['filtro']=filtro

   
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