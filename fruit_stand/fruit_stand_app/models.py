from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)



class Fruits(models.Model):
    tips_classification = (
        ('Extra', 'Extra'),
        ('De Primeira', 'De Primeira'),
        ('De Segunda', 'De Segunda'),
        ('De Terceira', 'De Terceira'),
    )

    tips_fresh = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length = 20, choices = tips_classification) 
    fresh = models.CharField(max_length = 3, choices = tips_fresh)  
    amount = models.PositiveIntegerField(blank=False)
    value = models.FloatField(blank=False)



class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100)
    fruit = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(blank=False)
    value = models.FloatField(blank=False)
    date = models.DateField(auto_now_add=True)