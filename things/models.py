from django.db import models

class Thing:
    def __init__(self, name, desc, quantity):
        self.name = name
        self.desc = desc
        self.quantity = quantity
