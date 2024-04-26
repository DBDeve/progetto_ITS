from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AccountManagers(models.Model):
  #user_id
  gestore=models.OneToOneField(User, on_delete=models.CASCADE)






# entrate
class Earnings(models.Model):
  #collegamenti inferiori
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  #dati tabella 
  Date=models.DateField("data di entrata", auto_now_add=True,null=True, blank=True)
  Quantity=models.DecimalField(default=0, max_digits=3, decimal_places=2)







class FarmHouses(models.Model):
  #collegamenti superiore
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  #dati agriturismo obbligatori 
  FarmHouseName=models.CharField(max_length=255)
  address=models.CharField(max_length=255)

class Rooms(models.Model):
    #collegamenti superiori
    IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
    #dati obbligatori
    stati_camera={
        "libera":"libera",
        "prenotata":"prenotata",
        "occupata": "occupata",
        "non disponibile":"non disponibile",}
    number = models.DecimalField(default=0, max_digits=3, decimal_places=0)
    prize = models.IntegerField( default=0)
    stato = models.CharField(max_length=15, choices=stati_camera, default="non disponibile")
    clienti_ospitabili=  models.IntegerField(default=0)
    #dati non obbligatori 
    appunto_gestore = models.CharField(max_length=200,default="") 
    appunti_cliente= models.CharField(max_length=200,default="") 
    #collegamenti
    #client = models.OneToOneField(Clients, on_delete = models.CASCADE,null=True,blank=True)

class Services(models.Model):
    #collegamenti superiori
    IdFarmHouses=models.ForeignKey(FarmHouses, on_delete = models.CASCADE)
    #datri servizzi
    name=models.CharField(max_length=200,default="")
    prize=models.IntegerField(default=0)
    NumberOfUse=models.IntegerField(default=0)

class Promotions(models.Model):
  IdFarmHouses=models.ForeignKey(FarmHouses, on_delete = models.CASCADE)
  #dati promozioni
  name=models.CharField(max_length=200,default="")
   #sconto
   #inizio
   #termine







#uscite
class Expense(models.Model):
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  Date=models.DateField("data spesa", auto_now_add=True,null=True, blank=True)
  Quantity=models.DecimalField(default=0, max_digits=3, decimal_places=2)





class Employee(models.Model):
  #collegamenti superiori
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  #dati tabella 
  name=models.CharField(max_length=200,default="")
  codice_fiscale=models.CharField(max_length=200, default="")
  iban=models.IntegerField(default=0)
  mail=models.CharField(max_length=200,default="")

class Salary(models.Model):
  #collegamenti superiori
  SalaryEmployee=models.ForeignKey(Employee, on_delete=models.CASCADE)
  SalaryGoOut=models.ForeignKey(Expense, on_delete=models.CASCADE)
  #dati tabella
  stipendio_ore=models.IntegerField(default=0)
  giorni_lavorati=models.IntegerField(default=0)
  ore_lavorate=models.IntegerField(default=0)





class Clients(models.Model):
  #collegamenti permanenti
  IdAccountManagers=models.ForeignKey(AccountManagers, on_delete=models.CASCADE)
  IdFarmHouses=models.ForeignKey(FarmHouses, on_delete=models.CASCADE)
  #collegamenti temporanei
  ClientRoom=models.OneToOneField(Rooms, on_delete=models.CASCADE,null=True, blank=True)
  ClientServices = models.ForeignKey(Services, on_delete=models.CASCADE,null=True, blank=True)
  #dati tabella
  name=models.CharField(default="",max_length=255,help_text = "*")
  mail=models.EmailField(default="", help_text = "*")
  number_cell=models.BigIntegerField(null=True, blank=True,help_text = "inserisci numero di telefono. puoi non metterlo ")
  frOm_data = models.DateField("data di arrivo", auto_now_add=True,null=True, blank=True)
  frOm_time = models.TimeField(null=True, blank=True)
  to = models.DateField(null=True, blank=True,help_text="data di partenza")
  to_time = models.TimeField(null=True, blank=True)
  visit_numbers=models.IntegerField(default=0)
  expense=models.IntegerField(default=0)



#se lo aggiungo dopo che la lista è stata creata posso fare solo due cosa:
    # 1. resettare il database e ricaricare tutto
    # 2. creare un clients e usare quel clients come default della foreinkey

#aggiungere classe promozioni con attributui: nome, sconto, validità,
  
#aggiungere classe entrate e uscite 



#mettere in nuova applicazione profile
# le foreing key vanno messe ai vari oggetti. non nell'oggetto profileGestore
