from django.db import models

from .models import User,AccountManagers,FarmHouses,Activity,TypeObjects,ActivityObject


# Create your models here.

#entrate
class Earnings(models.Model):
  #collegamenti 
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  IdActivity=models.ForeignKey(Activity, on_delete=models.CASCADE)
  #dati tabella 
  Date=models.DateField("data di entrata", auto_now_add=True,null=True, blank=True)
  Quantity=models.DecimalField(default=0, max_digits=8, decimal_places=2)

#uscite
class Expense(models.Model):
  #collegamenti
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  IdActivity=models.ForeignKey(Activity, on_delete=models.CASCADE)
  #dati tabella
  Date=models.DateField("data spesa", auto_now_add=True,null=True, blank=True)
  Quantity=models.DecimalField(default=0, max_digits=8, decimal_places= 2)





class Employee(models.Model):
  #collegamenti 
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  #dati tabella 
  name=models.CharField(max_length=200,default="")
  codice_fiscale=models.CharField(max_length=200, default="")
  iban=models.IntegerField(default=0)
  mail=models.CharField(max_length=200,default="")

class Clients(models.Model):
  #collegare alle attività
  #collegamenti permanenti
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey('FarmHouses', on_delete=models.CASCADE)
  #dati clienti
  name=models.CharField(default="",max_length=255,help_text = "*")
  mail=models.EmailField(default="", help_text = "*")
  number_cell=models.BigIntegerField(null=True, blank=True,help_text = "inserisci numero di telefono. puoi non metterlo ")





class Services(models.Model):
  #inserire collegamento ai singoli elementi delle attività
  #dati servizio
  name=models.CharField(max_length=200,default="")
  prize=models.IntegerField(default=0)
#promozioni
class Promotions(models.Model):
  #inserire collegamento ai singoli elementi delle attività
  #dati promozioni
  name=models.CharField(max_length=200,default="")
  sconto=models.CharField(max_length=200,default="")
