from django.db import models

#add namelist

class Thing:
    def __init__(self, name, description, quantity):
        if(length(name)>30 or length(name) == 0):
            raise ValueError()
        else:
            self.name = name

        if(length(description) > 120):
            raise ValueError()
        else:
            self.description = description

        if(quantity > 100 or quantity<0):
            raise ValueError()
        else:
            self.quantity = quantity
