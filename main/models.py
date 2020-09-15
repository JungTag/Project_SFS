from django.db import models
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
import requests

# Create your models here.
#class ExtendedUserInfo(models.Model):
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Site(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    tag = models.CharField(max_length=150)
    url = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=150, default=None)
    
    def __str__(self):
        return self.title