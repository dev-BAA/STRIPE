from django.db import models
from django.db.models import *


# Create your models here.
class Order(models.Model):
    name = TextField(null=True)

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = TextField(null=True)
    description = TextField(null=True)
    price = models.IntegerField()

class Tax(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = TextField(null=True)
    value = TextField(null=True)