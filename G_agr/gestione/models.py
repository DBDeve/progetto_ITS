from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AccountManagers(models.Model):
  #user_id
  gestore=models.OneToOneField(User, on_delete=models.CASCADE)





#modelli legati all'account e all'agriturismo

# entrate
class Earnings(models.Model):
  #collegamenti 
  IdAccountManagers=models.ForeignKey('AccountManagers', on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey('FarmHouses', on_delete=models.CASCADE)
  #dati tabella 
  Date=models.DateField("data di entrata", auto_now_add=True,null=True, blank=True)
  Quantity=models.DecimalField(default=0, max_digits=8, decimal_places=2)

#uscite
class Expense(models.Model):
  #collegamenti
  IdAccountManagers=models.ForeignKey('AccountManagers', on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey('FarmHouses', on_delete=models.CASCADE)
  #dati tabella
  Date=models.DateField("data spesa", auto_now_add=True,null=True, blank=True)
  Quantity=models.DecimalField(default=0, max_digits=8, decimal_places= 2)

#lavoratori
class Employee(models.Model):
  #collegamenti 
  IdAccountManagers=models.ForeignKey('AccountManagers', on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey('FarmHouses', on_delete=models.CASCADE)
  #dati tabella 
  name=models.CharField(max_length=200,default="")
  codice_fiscale=models.CharField(max_length=200, default="")
  iban=models.IntegerField(default=0)
  mail=models.CharField(max_length=200,default="")

#salari (collegato a lavoratori)
class Salary(models.Model):
  #collegamenti superiori
  SalaryEmployee=models.OneToOneField('Employee', on_delete=models.CASCADE)
  #dati tabella
  stipendio_ore=models.IntegerField(default=0)
  giorni_lavorati=models.IntegerField(default=0)
  ore_lavorate=models.IntegerField(default=0)

class Clients(models.Model):
  #collegamenti permanenti
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey('FarmHouses', on_delete=models.CASCADE)
  #dati clienti
  name=models.CharField(default="",max_length=255,help_text = "*")
  mail=models.EmailField(default="", help_text = "*")
  number_cell=models.BigIntegerField(null=True, blank=True,help_text = "inserisci numero di telefono. puoi non metterlo ")

class FarmHouses(models.Model):
  #collegamenti superiore
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  #dati agriturismo obbligatori 
  FarmHouseName=models.CharField(max_length=255)
  address=models.CharField(max_length=255)









#modelli collegati solo all'agriturismo (possibili attività dell'agriturismo)
#modello camere
class Rooms(models.Model):
    #collegamenti superiori
    IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
    #dati obbligatori
    stati_camera={
        "libera":"libera",
        "prenotata":"prenotata",
        "occupata": "occupata",
        "non disponibile":"non disponibile",}
    number = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    prize = models.IntegerField( default=0)
    stato = models.CharField(max_length=15, choices=stati_camera, default="non disponibile")
    clienti_ospitabili=  models.IntegerField(default=0)
    #dati non obbligatori 
    appunto = models.CharField(max_length=200,default="") 
#inserire modelli per tavoli, animali, bottiglie di vino




#modelli assiciati alle varie possibili attività dell'agriturismo
#servizzi
class Services(models.Model):
  #inserire collegamento alle attività
  #dati servizio
  name=models.CharField(max_length=200,default="")
  prize=models.IntegerField(default=0)
#promozioni
class Promotions(models.Model):
  #inserire collegamento alle attività
  #dati promozioni
  name=models.CharField(max_length=200,default="")
  sconto=models.CharField(max_length=200,default="")




#modelli per l'associazione dei dati
#modello prenotazioni
class Reservation(models.Model):
  #collegamenti
  IdAccountManager=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouse=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  #dati da associare (inserire anche le altre attività)
  IdRoom=models.OneToOneField(Rooms, on_delete=models.CASCADE)
  IdClient=models.OneToOneField(Clients, on_delete=models.CASCADE)
  #dati prenotazione (obbligatori)
  FrOmData = models.DateField("data di arrivo", auto_now_add=True,null=True, blank=True)
  ToData = models.DateField("data di partenza", auto_now_add=True,null=True, blank=True)

#modello visite
class visit(models.Model):
  #collegamenti   
  IdAccountManager=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouse=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  #dati da associare(inserire anche le altre attività)
  IdRoom=models.OneToOneField(Rooms, on_delete=models.CASCADE)
  IdClient=models.OneToOneField(Clients, on_delete=models.CASCADE)
  #dati visita
  visit_numbers=models.IntegerField(default=0)
  expense=models.IntegerField(default=0)