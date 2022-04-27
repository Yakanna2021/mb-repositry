from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=30,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=60,null=True,blank=True)
    state_province = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    website = models.URLField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    ph_numb = models.CharField(max_length=10,null=True,blank=True)
    
    


        
        