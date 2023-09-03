from django.db import models
from django.urls import reverse


# Create your models here.
class servicedb(models.Model):
    service_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="simage",null=True,blank=True)

class designdb(models.Model):
    Service=models.CharField(max_length=100,null=True,blank=True)
    Design_Name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="Dimage",null=True,blank=True)

class projectdb(models.Model):
    Project_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="pimage",null=True,blank=True)

class jobdb(models.Model):
    Position=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)

