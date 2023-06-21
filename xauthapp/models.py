from django.db import models
from django.contrib.auth.models import AbstractUser
from djongo import  models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username = models.CharField(unique=True,max_length=200)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200,null=True)
    videoUrl = models.URLField(max_length=200,null=False,default=None)
    type = models.CharField(max_length=100)
    duration = models.TimeField(default=None)
    price = models.DecimalField(max_digits=5,decimal_places=2)
