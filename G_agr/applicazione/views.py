
from django.shortcuts import HttpResponse

from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Hello world. questa è una prova")


def pagina(request):
    return HttpResponse("<html><body><h1> ciao</h1></body></html>")

#mi consente di inserire la pagine myfirst.html in view
def myfirst(request):
  import datetime

  x=datetime.datetime.now()

  template = loader.get_template('myfirst.html')

  context={'x': str(x),
     
  }

  return HttpResponse(template.render(context=context))

  