from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.template import loader

from .models import AccountManagers


# Create your views here.

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
         return redirect('login')
      except User.DoesNotExist:
         return redirect('cambia_password')
   
   template=loader.get_template('form_cambia_password.html')
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
      IdUser_id=user.id
      nuovo_account=AccountManagers(
         gestore_id=IdUser_id
      )
      nuovo_account.save()

      #rendirizza alla pagina di login
      return redirect('login')

   template=loader.get_template('form_registrati.html')
   return HttpResponse(template.render(context,request))



#fa accedere un utente già registrato
def log_in(request):
   if request.method=="POST":
      username = request.POST["username"]
      password = request.POST["password"]
      user = authenticate(request, username=username, password=password)
      #verifica che l'user sia stato autenticato
      if  user is not None:
         login(request, user)
         user_id=user.id
         account=AccountManagers.objects.get(gestore_id=user_id)
         account_id=account.id
         url=f"/principal_objects/{account_id}/agriturismo/verifica_aggiungi/None"
         return redirect(url)
      else:
         #return redirect('http://127.0.0.1:8000/gestione/visualizza/camere/tutte')
         return render(request, "form_accedi.html", {"argomento":'log in | accedi'})
   else:
      return render(request, "form_accedi.html", {"argomento":'log in | accedi'})



#fa fare il logout e rendirizza alla pagina di login
def log_out(request):
   logout(request)
   return redirect('login')