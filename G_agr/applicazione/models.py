from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content= models.TextField()
    #come viene scritto nell'amministrazione 
    def __str__(self):
        return self.user.first_name + "" + self.user.last_name + "(" + self.user.username+")"

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Clients(models.Model):
  name=models.CharField(default="",max_length=255,help_text = "*")
  mail=models.EmailField(default="", help_text = "*")
  number_cell=models.BigIntegerField(null=True, blank=True,help_text = "inserisci numero di telefono. puoi non metterlo ")
  frOm_data = models.DateField("data di arrivo", auto_now_add=True,null=True, blank=True)
  frOm_time = models.TimeField(null=True, blank=True)
  to_date = models.DateField("data di partenza", auto_now_add=True,null=True, blank=True)
  to_time = models.TimeField(null=True, blank=True)
  visit_numbers=models.IntegerField(default=0)
  expense=models.IntegerField(default=0)

  #def add_clients(self,name,mail,number_cell):
     

  def cambia_mail(self,nuova_mail):
     self.mail=nuova_mail
  



class Room(models.Model):
    #dati obbligatori
    stati_camera={
        "libera":"libera",
        "prenotata":"prenotata",
        "occupata": "occupata",
        "non disponibile":"non disponibile",}
    number = models.IntegerField(default=0)
    prize = models.IntegerField(default=0)
    stato = models.CharField(max_length=15, choices=stati_camera, default="non disponibile")
    clienti_ospitabili=  models.IntegerField(default=0)
    #dati non obbligatori 
    appunto_gestore = models.CharField(max_length=200,default="") 
    appunti_cliente= models.CharField(max_length=200,default="") 
    #collegamenti
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
       


class services(models.Model):
    prize=models.IntegerField(default=0)
    NumberOfUse=models.IntegerField(default=0)

class employee(models.Model):
  name=models.CharField(max_length=200,default="")
  codice_fiscale=models.CharField(max_length=200, default="")
  iban=models.IntegerField(default=0)
  mail=models.CharField(max_length=200,default="")

class stipendio(models.Model):
  stipendio_ore=models.IntegerField(default=0)
  giorni_lavorati=models.IntegerField(default=0)
  ore_lavorate=models.IntegerField(default=0)

class promotions(models.Model):
   name=models.CharField(max_length=200,default="")
   #sconto
   #inizio
   #termine

#se lo aggiungo dopo che la lista è stata creata posso fare solo due cosa:
    # 1. resettare il database e ricaricare tutto
    # 2. creare un clients e usare quel clients come default della foreinkey

#aggiungere classe promozioni con attributui: nome, sconto, validità,
  
#aggiungere classe entrate e uscite 