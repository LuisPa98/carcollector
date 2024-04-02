from django.db import models

# Create your models here.
class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=25)
    description = models.TextField(max_length=350)
    price = models.IntegerField()
    def __str__(self):
        return self.name