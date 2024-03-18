
from django.shortcuts import HttpResponse

from django.template import loader

#importa il modello question
from .models import Question,Room

# Create your views here.

def index(request):
    return HttpResponse("Hello world. questa è una prova")


def pagina(request):
    return HttpResponse("<html><body><h1> ciao</h1></body></html>")

#mi consente di inserire la pagine myfirst.html in view
def myfirst(request):
  import datetime
  
  #mette tutti valori del modello Question nella variabile questions
  questions = Question.objects.all().values()

  x=datetime.datetime.now()
  nome='dario'

  template = loader.get_template('myfirst.html')

  context={
    'x': str(x),
    'nome':nome,
    'questions':questions,
  }

  return HttpResponse(template.render(context=context))

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())




def camere(request):
   camere = Room.objects.all().values()
   
   context={
      'camere': camere
   }

   template=loader.get_template('camere.html')
   return HttpResponse(template.render(context=context))

  