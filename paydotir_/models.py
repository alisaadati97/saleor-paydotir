from django.db import models

# Create your models here.

class Paydotir(models.Model):
    
    username = models.CharField(max_length=20,blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=30,blank=True, null=True)
    transid = models.CharField(max_length=30,blank=True, null=True)