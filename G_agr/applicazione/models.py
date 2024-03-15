from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Room(models.Model):
    number = models.IntegerField(default=0)
    prize = models.IntegerField(default=0)
    da = models.DateTimeField("data di arrivo")
    a = models.DateTimeField("data di partenza")
    appunto = models.CharField(max_length=200) 
    cliente_occupante = models.CharField (max_length=200)


