from django.db import models

class Thing:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity
