from django.db import models

#add namelist

class Thing(models.Model):
    if(len(models.name)>30 or len(models.name) == 0):
        raise ValueError()
    else:
        self.name = models.name

    if(len(models.description) > 120):
        raise ValueError()
    else:
        self.description = models.description

    if(models.quantity > 100 or models.quantity<0):
        raise ValueError()
    else:
        self.quantity = models.quantity
