from django.db import models

# Create your models here.

class article(models.Model):
   
    nom = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    prix= models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
