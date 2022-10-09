from django.db import models

#add namelist

class Thing(models.Model):

    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120)
    quantity = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)])
