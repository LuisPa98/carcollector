from django.db import models
from django.contrib.auth.models import User

AGE = (
    ('<1', 'Less than a year old'),
    ('2-4', 'Between 2-4 years old'),
    ('5+', 'More than 5 years old')
)

TYPE = (
    ('Nylon', 'Nylon'),
    ('Cotton', 'Cotton'),
    ('Polyester', 'Polyester'),
    ('Raw Hide', 'Raw Hide')
)

# Create your models here.
class Shoelace(models.Model):
    shoelacetype = models.CharField(
        max_length=10,
        choices=TYPE,
        default=TYPE[0][0]
    )
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.shoelacetype

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=25)
    description = models.TextField(max_length=350)
    price = models.IntegerField()
    shoelace = models.ManyToManyField(Shoelace)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Worn(models.Model):
    date = models.DateField('Enter Date Bought')
    age = models.CharField(
        max_length=5,
        choices=AGE,
        default=AGE[0][0]
        )

    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    def __str__(self):
        return f'Bought on {self.date} and is {self.age} years old '

