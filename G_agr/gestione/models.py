from django.db import models
from applicazione.models import Clients


# Create your models here.

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
    client = models.OneToOneField(Clients, on_delete = models.CASCADE,null=True,blank=True)
    

class services(models.Model):
    name=models.CharField(max_length=200,default="")
    prize=models.IntegerField(default=0)
    NumberOfUse=models.IntegerField(default=0)
    client = models.ForeignKey(Clients, on_delete = models.CASCADE)

class promotions(models.Model):
   name=models.CharField(max_length=200,default="")
   client = models.ForeignKey(Clients, on_delete = models.CASCADE)
   #sconto
   #inizio
   #termine





class employee(models.Model):
  name=models.CharField(max_length=200,default="")
  codice_fiscale=models.CharField(max_length=200, default="")
  iban=models.IntegerField(default=0)
  mail=models.CharField(max_length=200,default="")

class stipendio(models.Model):
  stipendio_ore=models.IntegerField(default=0)
  giorni_lavorati=models.IntegerField(default=0)
  ore_lavorate=models.IntegerField(default=0)



#se lo aggiungo dopo che la lista è stata creata posso fare solo due cosa:
    # 1. resettare il database e ricaricare tutto
    # 2. creare un clients e usare quel clients come default della foreinkey

#aggiungere classe promozioni con attributui: nome, sconto, validità,
  
#aggiungere classe entrate e uscite 