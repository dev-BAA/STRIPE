from django.db import models
from django.db.models import *


# Create your models here.
class Item(models.Model):
    name = TextField(null=True)
    description = TextField(null=True)
    price = models.IntegerField()
