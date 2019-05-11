from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=16,primary_key=True)
    pwd = models.CharField(max_length=16)
    age = models.IntegerField(default=0)
