from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.TextField(default='')