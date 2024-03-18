from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Clients(models.Model):
  name=models.CharField(max_length=200)
  visit_numbers=models.IntegerField(default=0)
  expense=models.IntegerField(default=0)

class Room(models.Model):
    stati_camera={
        "L":"libera",
        "O": "occupata",
        "ND":"non disponibile",}
    number = models.IntegerField(default=0)
    prize = models.IntegerField(default=0)
    da = models.DateTimeField("data di arrivo")
    to = models.DateTimeField("data di partenza")
    stato = models.CharField(max_length=10, choices=stati_camera, default="ND")
    appunto = models.CharField(max_length=200) 

class services(models.Model):
  prize=models.IntegerField(default=0)
  NumberOfUse=models.IntegerField(default=0)

class employee(models.Model):
  name=models.CharField(max_length=200)
  stipendio_ore=models.IntegerField(default=0)
  stipendio_mese=models.IntegerField(default=0)
  giorni_lavoro=models.IntegerField(default=0)
  ore_lavorate=models.IntegerField(default=0)