from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField
  lastname = models.CharField
  id=models.IntegerField
  email = models.CharField
  password = models.CharField
    

#modello delle camere.
class room(models.Model):
  number=models.IntegerField
  prize=models.IntegerField
  da=models.IntegerField
  a=models.IntegerField
  appunto=models.IPAddressField
  status=models.CharField
  cliente_occupante=models.CharField


#modello dei servizzi
class services(models.model):
  name=models.CharField
  prize=models.IntegerField
  NumberOfUse=models.IntegerField


#modello dei clienti
class Clients(models.Models):
  name=models.CharField
  Nprenotazione=models.IntegerField
  expense=models.IntegerField

#modello dei lavoratori
class employee:
  name=models.CharField
  stipendio_ore=models.IntegerField
  stipendio_mese=models.IntegerField
  giorni_lavoro=models.IntegerField
  ore_lavorate=models.IntegerField


class promotions:
  name=models.CharField
  sconto=models.BigIntegerField 
