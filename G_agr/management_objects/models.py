from django.db import models

#from management_objects.models import AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject
#from register_objects.models  import Clients
# Create your models here.

#modello prenotazioni
class Reservation(models.Model):
  #inserire collegamento alle attività
  #collegamenti
  IdActivity=models.ForeignKey('principal_objects.Activity', on_delete=models.CASCADE)
  #dati da associare (inserire anche le altre attività)
  IdActivityObject=models.OneToOneField('principal_objects.ActivityObject', on_delete=models.CASCADE)
  IdClient=models.OneToOneField('register_objects.Clients', on_delete=models.CASCADE)
  #dati prenotazione (obbligatori)
  FrOmData = models.DateField("data di arrivo", auto_now_add=True,null=True, blank=True)
  ToData = models.DateField("data di partenza", auto_now_add=True,null=True, blank=True)

#modello visite
class visit(models.Model):
  #collegamenti   
  IdAccountManager=models.ForeignKey('principal_objects.AccountManagers', on_delete=models.CASCADE)
  IdFarmHouse=models.ForeignKey('principal_objects.FarmHouses', on_delete=models.CASCADE)
  #dati da associare(inserire anche le altre attività)
  #IdRoom=models.OneToOneField(Rooms, on_delete=models.CASCADE)
  IdClient=models.OneToOneField('register_objects.Clients', on_delete=models.CASCADE)
  #dati visita
  visit_numbers=models.IntegerField(default=0)
  expense=models.IntegerField(default=0)
