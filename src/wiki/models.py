from django.db import models

# Create your models here.
class Queries(models.Model):
    #user_id = models.CharField(max_length=200, default='cheikhou')
    query = models.CharField(max_length=200)