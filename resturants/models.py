from django.db import models
from datetime import datetime

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="")
    opening_time = models.IntegerField()
    closing_time = models.IntegerField()
    created_at = models.DateTimeField(default= datetime.now(), blank= True) 