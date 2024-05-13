from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class AccountManagers(models.Model):
  #user_id
  gestore=models.OneToOneField(User, on_delete=models.CASCADE)

#accont è collegato agli agriturismi 

class FarmHouses(models.Model):
  #collegamenti superiore
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  #dati agriturismo obbligatori 
  FarmHouseName=models.CharField(max_length=255)
  address=models.CharField(max_length=255)

#agriturismi sono collegati alle attività

class Activity(models.Model): #esempio: ristorante
  IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  ActivityType=models.CharField(max_length=255)
  ActivityName=models.CharField(max_length=255)

#le attività sono collegate ad un gruppo di oggetti

class TypeObjects(models.Model):
  IdActivity=models.ForeignKey(Activity, on_delete=models.CASCADE)
  TypeName=models.CharField(max_length=255)

#il gruppo di oggetti si collega ai vari oggetti del gruppo

class ActivityObject(models.Model): 
  IdTypeObjects=models.ForeignKey(TypeObjects, on_delete=models.CASCADE)
  ObjectNumber = models.IntegerField( default=0)
  ObjectPrize=models.DecimalField(default=0, max_digits=8, decimal_places=2)
  stati_oggetto={
    "libera":"libera",
    "prenotata":"prenotata",
    "occupata": "occupata",
    "non disponibile":"non disponibile",}
  stato = models.CharField(max_length=15, choices=stati_oggetto, default="non disponibile")