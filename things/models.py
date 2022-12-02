from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#add namelist

class Thing(models.Model):

    name = models.CharField(max_length=30, min_length=1, unique=True)
    description = models.CharField(max_length=120)
    quantity = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)])
